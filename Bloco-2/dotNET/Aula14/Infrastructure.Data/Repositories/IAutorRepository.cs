using Infrastructure.Data.Models;
using System.Collections.Generic;

namespace Infrastructure.Data.Repositories {
    interface IAutorRepository {
        IEnumerable<AutorModel> GetAll(string search);
        AutorModel GetById(int id);
        AutorModel Create(AutorModel autorModel);
        AutorModel Edit(AutorModel autorModel);
        void Delete(int id);
    }
}
