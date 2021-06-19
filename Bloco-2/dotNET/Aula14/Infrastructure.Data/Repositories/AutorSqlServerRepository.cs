using Infrastructure.Data.Models;
using Microsoft.Data.SqlClient;
using System;
using System.Collections.Generic;
using System.Data;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Infrastructure.Data.Repositories {
    public class AutorSqlServerRepository : IAutorRepository  {
        private const string ConnectionString =
            "Data Source=(localdb)\\MSSQLLocalDB;Initial Catalog=GRLEDC21N1sql;Integrated Security=True;Connect Timeout=30;Encrypt=False;TrustServerCertificate=False;ApplicationIntent=ReadWrite;MultiSubnetFailover=False";

        public AutorModel Create(AutorModel autorModel) {
            using SqlConnection sqlConnection = new SqlConnection(ConnectionString);
            sqlConnection.Open();
            var command = sqlConnection.CreateCommand();
           
            command.CommandType = CommandType.Text;
            command.CommandText =
            @"INSERT INTO Autor
                (Nome, UltimoNome, Nacionalidade, QuantidadeLivrosPublicados, Nascimento)
                OUTPUT INSERTED.Id
	            VALUES(@nome, @ultimoNome, @nacionalidade, @quantidadeLivrosPublicados, @nascimento);";

            command.Parameters
                .Add("@nome", SqlDbType.NVarChar)
                .Value = autorModel.Nome;
            command.Parameters
                .Add("@ultimoNome", SqlDbType.NVarChar)
                .Value = autorModel.UltimoNome;
            command.Parameters
                .Add("@nacionalidade", SqlDbType.NVarChar)
                .Value = autorModel.Nacionalidade;
            command.Parameters
                .Add("@quantidadeLivrosPublicados", SqlDbType.Int)
                .Value = autorModel.QuantidadeLivrosPublicados;
             command.Parameters
                .Add("@nascimento", SqlDbType.DateTime2)
                .Value = autorModel.Nascimento;

            try {
                command.ExecuteScalar();
                return autorModel;
            }
            catch {
                return null;
            }

            
        }

        public void Delete(int id) {
            using SqlConnection sqlConnection = new SqlConnection(ConnectionString);
            sqlConnection.Open();
            var command = sqlConnection.CreateCommand();

            command.CommandType = CommandType.Text;
            command.CommandText =
                 @"DELETE FROM Autor WHERE Id = @id";
            command.Parameters
               .Add("@id", SqlDbType.Int)
               .Value = id;

            command.ExecuteScalar();
        }

        public AutorModel Edit(AutorModel autorModel) {
            using SqlConnection sqlConnection = new SqlConnection(ConnectionString);
            sqlConnection.Open();

            var command = sqlConnection.CreateCommand();

            command.CommandType = CommandType.Text;
            command.CommandText =
                @"UPDATE Autor
                SET Nome = @nome, UltimoNome = @ultimoNome, Nacionalidade = @nacionalidade, 
                    QuantidadeLivrosPublicados = @quantidadeLivrosPublicados, Nascimento = @nascimento
	            WHERE Id = @id;";

            command.Parameters
                .Add("@nome", SqlDbType.NVarChar)
                .Value = autorModel.Nome;
            command.Parameters
                .Add("@ultimoNome", SqlDbType.NVarChar)
                .Value = autorModel.UltimoNome;
            command.Parameters
                .Add("@nacionalidade", SqlDbType.NVarChar)
                .Value = autorModel.Nacionalidade;
            command.Parameters
                .Add("@quantidadeLivrosPublicados", SqlDbType.Int)
                .Value = autorModel.QuantidadeLivrosPublicados;
            command.Parameters
               .Add("@nascimento", SqlDbType.DateTime2)
               .Value = autorModel.Nascimento;
            command.Parameters
               .Add("@id", SqlDbType.Int)
               .Value = autorModel.Id;

            command.ExecuteScalar();

            return autorModel;
        }

        public IEnumerable<AutorModel> GetAll(string search) {
            using SqlConnection sqlConnection = new SqlConnection(ConnectionString);
            sqlConnection.Open();
            var command = sqlConnection.CreateCommand();
            command.CommandType = CommandType.Text;
            
            var commandText = "SELECT * FROM Autor";
            if (!string.IsNullOrWhiteSpace(search)) {
                commandText += " WHERE Nome LIKE @search OR UltimoNome LIKE @search";
                command.Parameters
                    .Add("@search", SqlDbType.NVarChar)
                    .Value = "%" + search + "%";
            }

            command.CommandText = commandText;

            var reader = command.ExecuteReader();

            var autores = new List<AutorModel>();
            
            while (reader.Read()) {
                var autor = new AutorModel {
                    Id = reader.GetFieldValue<int>("Id"),
                    Nacionalidade = reader.GetFieldValue<string>("Nacionalidade"),
                    Nascimento = reader.GetFieldValue<DateTime>("Nascimento"),
                    Nome = reader.GetFieldValue<string>("Nome"),
                    UltimoNome = reader.GetFieldValue<string>("UltimoNome"),
                    QuantidadeLivrosPublicados = reader.GetFieldValue<int>("QuantidadeLivrosPublicados")
                };
                autores.Add(autor);
            }

            return autores;

            //if (search == null) {
            //    return autores;
            //}
            //else {
            //    return autores.Where(x =>
            //        x.Nome.Contains(search, StringComparison.OrdinalIgnoreCase) ||
            //        x.UltimoNome.Contains(search, StringComparison.OrdinalIgnoreCase));
            //}
        }

        public AutorModel GetById(int id) {
            using SqlConnection sqlConnection = new SqlConnection(ConnectionString);
            sqlConnection.Open();
            var command = sqlConnection.CreateCommand();
            command.CommandType = CommandType.Text;
            command.CommandText = "SELECT * FROM Autor WHERE Id = @id;";

            command.Parameters
                .Add("@id", SqlDbType.Int)
                .Value = id;

            var reader = command.ExecuteReader();
            var canRead = reader.Read();

            if (!canRead) {
                return null;
            }

            var autor = new AutorModel {
                Id = reader.GetFieldValue<int>("Id"),
                Nacionalidade = reader.GetFieldValue<string>("Nacionalidade"),
                Nascimento = reader.GetFieldValue<DateTime>("Nascimento"),
                Nome = reader.GetFieldValue<string>("Nome"),
                UltimoNome = reader.GetFieldValue<string>("UltimoNome"),
                QuantidadeLivrosPublicados = reader.GetFieldValue<int>("QuantidadeLivrosPublicados")
            };

            return autor;
            
        }
    }
}
