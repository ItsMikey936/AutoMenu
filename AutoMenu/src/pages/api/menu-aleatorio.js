import pool from '../../db.js';

export async function GET() {
  const [dias] = await pool.query('SELECT * FROM dias ORDER BY id_Dia');
  const [tiposComida] = await pool.query('SELECT * FROM tipos_Comida ORDER BY id_Tipos_Comida');

  const menuTable = {};

  for (const tipo of tiposComida) {
    // Obtén todos los platillos posibles para este tipo de comida
    const [platillos] = await pool.query(
      `SELECT DISTINCT p.nombre_Platillo
       FROM Platillos p
       JOIN menus m ON m.id_Platillo = p.id_Platillo
       WHERE m.id_Tipos_Comida = ?`,
      [tipo.id_Tipos_Comida]
    );

    // Mezcla los platillos 
    let platillosShuffle = [...platillos].sort(() => Math.random() - 0.5);
    if (platillosShuffle.length < dias.length) {
      while (platillosShuffle.length < dias.length) {
        platillosShuffle.push({ nombre_Platillo: '' });
      }
    } else {
      platillosShuffle = platillosShuffle.slice(0, dias.length);
    }

    menuTable[tipo.nombre_Tipo] = {};
    dias.forEach((dia, idx) => {
      menuTable[tipo.nombre_Tipo][dia.dia] = platillosShuffle[idx]?.nombre_Platillo || '';
    });
  }

  return new Response(JSON.stringify({ menuTable, dias, tiposComida }), {
    headers: { 'Content-Type': 'application/json' }
  });
}