import type { APIRoute } from 'astro'
import pool from '../../db.js'

export const GET: APIRoute = async ({ request }) => {
  const url = new URL(request.url)
  const tipo = Number(url.searchParams.get('tipo')) || 0

  if (![5, 6].includes(tipo)) {
    return new Response(JSON.stringify({ error: 'ID inválido' }), { status: 400 })
  }

  try {
    const [ingredientes] = await pool.query(`
      SELECT * FROM Ingredientes WHERE id_Tipo_Ingrediente = ?
    `, [tipo])

    return new Response(JSON.stringify({ ingredientes }), {
      headers: { 'Content-Type': 'application/json' }
    })
  } catch (err: any) {
    console.error('Error consultando ingredientes:', err)
    return new Response(JSON.stringify({ error: err.message }), { status: 500 })
  }
}
