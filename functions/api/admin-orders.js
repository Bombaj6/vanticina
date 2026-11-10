// functions/api/admin-orders.js - View & export orders stored in D1

export async function onRequestGet(context) {
  const url = new URL(context.request.url);
  const secretKey = url.searchParams.get('key');
  const format = url.searchParams.get('format') || 'html';

  const ADMIN_KEY = (context.env && context.env.ADMIN_KEY) || 'vantacin2026';

  if (secretKey !== ADMIN_KEY) {
    return new Response('Unauthorized: Please provide the valid ?key= parameter.', {
      status: 401,
      headers: { 'Content-Type': 'text/plain' }
    });
  }

  if (!context.env || !context.env.DB) {
    return new Response('D1 Database binding not found.', { status: 500 });
  }

  try {
    const { results } = await context.env.DB.prepare(
      'SELECT * FROM orders ORDER BY id DESC'
    ).all();

    if (format === 'json') {
      return new Response(JSON.stringify(results, null, 2), {
        headers: { 'Content-Type': 'application/json' }
      });
    }

    if (format === 'csv') {
      const headers = ['Order Ref', 'Date (UTC)', 'Name', 'Phone', 'Alt Phone', 'Address', 'City', 'State', 'Package', 'Amount', 'Payment Method', 'Status'];
      const csvRows = [headers.join(',')];
      for (const row of results) {
        const values = [
          `"${row.order_ref || ''}"`,
          `"${row.created_at || ''}"`,
          `"${(row.name || '').replace(/"/g, '""')}"`,
          `"${row.phone || ''}"`,
          `"${row.alt_phone || ''}"`,
          `"${(row.address || '').replace(/"/g, '""')}"`,
          `"${(row.city || '').replace(/"/g, '""')}"`,
          `"${row.state || ''}"`,
          `"${(row.package || '').replace(/"/g, '""')}"`,
          row.amount || 0,
          `"${row.payment_method || 'COD'}"`,
          `"${row.payment_status || 'pending'}"`
        ];
        csvRows.push(values.join(','));
      }
      return new Response(csvRows.join('\n'), {
        headers: {
          'Content-Type': 'text/csv; charset=utf-8',
          'Content-Disposition': 'attachment; filename="vantacin_orders.csv"'
        }
      });
    }

    // Default: Responsive HTML Dashboard
    const rowsHtml = results.length === 0
      ? '<tr><td colspan="10" style="text-align:center; padding:30px; color:#666;">No orders recorded yet.</td></tr>'
      : results.map(o => `
        <tr>
          <td><strong style="color:#059669;">${o.order_ref || 'VAN-' + o.id}</strong></td>
          <td style="font-size:12px; color:#64748b;">${o.created_at}</td>
          <td><strong>${o.name}</strong></td>
          <td>
            <a href="tel:${o.phone}" style="color:#0284c7; text-decoration:none;">${o.phone}</a>
            ${o.alt_phone ? `<br><small style="color:#64748b;">Alt: <a href="https://wa.me/${o.alt_phone.replace(/[^0-9]/g,'')}" target="_blank">${o.alt_phone}</a></small>` : ''}
          </td>
          <td>${o.address}, ${o.city ? o.city + ', ' : ''}<strong>${o.state}</strong></td>
          <td><span style="display:inline-block; padding:3px 8px; border-radius:4px; background:#f1f5f9; font-weight:600; font-size:12px;">${o.package}</span></td>
          <td style="font-weight:700; color:#0f172a;">₦${Number(o.amount || 0).toLocaleString()}</td>
          <td><span style="display:inline-block; padding:3px 8px; border-radius:4px; background:#e0f2fe; color:#0369a1; font-weight:600; font-size:12px;">${o.payment_method}</span></td>
          <td><span style="display:inline-block; padding:3px 8px; border-radius:4px; background:#fef3c7; color:#92400e; font-weight:600; font-size:12px;">${o.payment_status}</span></td>
          <td>
            <a href="https://wa.me/${o.phone.replace(/[^0-9]/g, '')}?text=Hello%20${encodeURIComponent(o.name)}%2C%20this%20is%20Customer%20Care%20regarding%20your%20order%20for%20Vantacin%2B." target="_blank" style="display:inline-block; padding:6px 12px; background:#25D366; color:#fff; border-radius:6px; font-weight:700; text-decoration:none; font-size:12px;">WhatsApp Dispatch 💬</a>
          </td>
        </tr>
      `).join('');

    const html = `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>VANTACIN+ Orders Manager</title>
  <style>
    * { box-sizing: border-box; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; }
    body { background: #f8fafc; margin: 0; padding: 20px; color: #1e293b; }
    .container { max-width: 1400px; margin: 0 auto; background: #fff; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.06); padding: 25px; }
    .header { display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid #e2e8f0; padding-bottom: 15px; margin-bottom: 20px; flex-wrap: wrap; gap: 15px; }
    .header h1 { margin: 0; font-size: 22px; color: #0f172a; display: flex; align-items: center; gap: 10px; }
    .actions { display: flex; gap: 10px; }
    .btn { padding: 8px 16px; border-radius: 6px; font-size: 13px; font-weight: 700; text-decoration: none; cursor: pointer; border: none; }
    .btn-csv { background: #059669; color: #fff; }
    .btn-refresh { background: #f1f5f9; color: #334155; }
    table { width: 100%; border-collapse: collapse; font-size: 13px; }
    th { background: #f1f5f9; padding: 12px 10px; text-align: left; color: #475569; font-weight: 700; border-bottom: 1px solid #cbd5e1; }
    td { padding: 12px 10px; border-bottom: 1px solid #f1f5f9; vertical-align: middle; }
    tr:hover td { background: #fafaf9; }
    .stat-badge { background: #dcfce7; color: #166534; font-weight: 700; padding: 4px 10px; border-radius: 20px; font-size: 13px; }
  </style>
</head>
<body>
  <div class="container">
    <div class="header">
      <div>
        <h1>💊 VANTACIN+ Order Database <span class="stat-badge">${results.length} Total Orders</span></h1>
        <p style="margin: 5px 0 0; color: #64748b; font-size: 13px;">Direct real-time submissions stored on Cloudflare D1</p>
      </div>
      <div class="actions">
        <a href="?key=${secretKey}&format=csv" class="btn btn-csv">📥 Download CSV for Excel</a>
        <a href="?key=${secretKey}" class="btn btn-refresh">🔄 Refresh Orders</a>
      </div>
    </div>
    <div style="overflow-x: auto;">
      <table>
        <thead>
          <tr>
            <th>Ref</th>
            <th>Date & Time</th>
            <th>Customer Name</th>
            <th>Contact</th>
            <th>Delivery Address</th>
            <th>Package</th>
            <th>Amount</th>
            <th>Payment</th>
            <th>Status</th>
            <th>Action</th>
          </tr>
        </thead>
        <tbody>
          ${rowsHtml}
        </tbody>
      </table>
    </div>
  </div>
</body>
</html>`;

    return new Response(html, {
      headers: { 'Content-Type': 'text/html; charset=utf-8' }
    });
  } catch (err) {
    return new Response('Database error: ' + err.message, { status: 500 });
  }
}
