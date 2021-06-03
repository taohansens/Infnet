using System;
using System.Collections.Generic;
using System.Linq;

namespace Infrastructure.Data.Repositories {
    public class AutorInMemoryRepository : IAutorRepository {

        private static List<AutorModel> Autores { get; } = new List<AutorModel> {
            new AutorModel {
                Id = 1,
                Nome="Tao",
                UltimoNome = "Hansen",
                Nacionalidade = "Brasileiro",
                Nascimento = new DateTime(1996, 01, 31),
                QuantidadeLivrosPublicados = 1
            },
            new AutorModel {
                Id = 2,
                Nome="Felipe",
                UltimoNome = "Andrade",
                Nacionalidade = "Brasileiro",
                Nascimento = new DateTime(1988, 04, 12),
                QuantidadeLivrosPublicados = 10
            },
        };

        public AutorModel Create(AutorModel autorModel) {
            autorModel.Id = GetAll().Count() + 1;
            Autores.Add(autorModel);
            return autorModel;
        }

        public void Delete(int id) {
            var autor = GetById(id);
            if (autor != null) {
                Autores.Remove(autor);
            }
        }

        public AutorModel Edit(AutorModel autorModel) {
            var autor = GetById(autorModel.Id);
            if (autor != null) {
                autor.Id = autorModel.Id;
                autor.Nome = autorModel.Nome;
                autor.UltimoNome = autorModel.UltimoNome;
                autor.Nacionalidade = autorModel.Nacionalidade;
                autor.QuantidadeLivrosPublicados = autorModel.QuantidadeLivrosPublicados;
                return autor;
            }
            else {
                return null;
            }

        }

        public IEnumerable<AutorModel> GetAll() {
            return Autores;
        }

        public AutorModel GetById(int id) {
            var autor = Autores.FirstOrDefault(x => x.Id == id);
            if (autor != null) {
                return autor;
            }
            else {
                return null;
            };
        }
    }
}
