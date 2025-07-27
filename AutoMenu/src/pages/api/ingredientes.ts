import type { APIRoute } from "astro"
import pool from "../../db.js"

export const GET: APIRoute = async () => {
  try {
    const [ingredientes] = await pool.query(`
      SELECT 
        i.id_Ingrediente,
        i.nombre_Ingrediente,
        i.unidad_Ingrediente,
        i.porcion_Ingrediente,
        i.id_Tipo_Ingrediente,
        t.nombre_Tipo_Ingrediente
      FROM Ingredientes i
      JOIN Tipos_Ingredientes t ON i.id_Tipo_Ingrediente = t.id_Tipo_Ingrediente
      ORDER BY t.id_Tipo_Ingrediente, i.nombre_Ingrediente
    `)

    // Organizar ingredientes por tipo
    const ingredientesPorTipo = {
      1: [], // Vegetales
      2: [], // Origen Animal
      3: [], // Leguminosas
      4: [], // Frutas
      5: [], // Cereales
      6: [], // Aceites y grasas
      7: [], // Lacteos
      8: [], // Grasas con proteina
      9: [], // Azucar
    }

    ingredientes.forEach((ingrediente) => {
      ingredientesPorTipo[ingrediente.id_Tipo_Ingrediente].push(ingrediente)
    })

    return new Response(JSON.stringify(ingredientesPorTipo), {
      headers: { "Content-Type": "application/json" },
    })
  } catch (error) {
    console.error("Error al obtener ingredientes:", error)
    return new Response(JSON.stringify({ error: "Error interno del servidor" }), {
      status: 500,
      headers: { "Content-Type": "application/json" },
    })
  }
}
