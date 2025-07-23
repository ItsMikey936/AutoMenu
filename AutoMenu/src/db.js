import mysql from 'mysql2/promise';

const pool = mysql.createPool({
  host: 'localhost',
  user: 'root',      // Cambia si tienes otro usuario
  password: '',      // Cambia si tienes contraseña
  database: 'automenu', // Cambia por el nombre real
});

export default pool;