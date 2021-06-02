using Aula08Crud.Models;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Aula08Crud.Controllers {
    public class AutorController : Controller {
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

        // GET: AutorController
        public ActionResult Index() {
            return View(Autores);
        }

        // GET: AutorController/Details/5
        public ActionResult Details(int id) {
            var autorModel = Autores.FirstOrDefault(x => x.Id == id);
            
 //           foreach (var autor in Autores) {
 //               if (autor.Id == id) {
 //                   return View(autor);
 //               } else {
 //                   return RedirectToAction(nameof(Index));
 //               }
 //           }
            
            if (autorModel != null) {
                return View(autorModel);
            }
            else {
                return RedirectToAction(nameof(Index));
            }
        }

        // GET: AutorController/Create
        public ActionResult Create() {
            return View();
        }

        // POST: AutorController/Create
        [HttpPost]
        [ValidateAntiForgeryToken]
        public ActionResult Create(AutorModel autorModel) {
            try {
                Autores.Add(autorModel);
                return RedirectToAction(nameof(Index));
            }
            catch {
                return View();
            }
        }

        // GET: AutorController/Edit/5
        public ActionResult Edit(int id) {
            var autorModel = Autores.FirstOrDefault(x => x.Id == id);

            if (autorModel != null) {
                return View(autorModel);
            }
            else {
                return RedirectToAction(nameof(Index));
            }
        }

        // POST: AutorController/Edit/5
        [HttpPost]
        [ValidateAntiForgeryToken]
        public ActionResult Edit(int id, AutorModel autorModel) {
            try {
                var autor = Autores.FirstOrDefault(x => x.Id == id);
                EditAutor(autor, autorModel);

                return RedirectToAction(nameof(Details), new { id = autor.Id });
            }
            catch {
                return View();
            }
        }

        public AutorModel EditAutor(AutorModel autor, AutorModel autorEdit) {
            autor.Id = autorEdit.Id;
            autor.Nome = autorEdit.Nome;
            autor.UltimoNome = autorEdit.UltimoNome;
            autor.Nacionalidade = autorEdit.Nacionalidade;
            autor.QuantidadeLivrosPublicados = autorEdit.QuantidadeLivrosPublicados;
            return autor;

        }

        // GET: AutorController/Delete/5
        public ActionResult Delete(int id) {
            var autorModel = Autores.FirstOrDefault(x => x.Id == id);

            if (autorModel != null) {
                return View(autorModel);
            }
            else {
                return RedirectToAction(nameof(Index));
            }
        }

        // POST: AutorController/Delete/5
        [HttpPost]
        [ValidateAntiForgeryToken]
        public ActionResult Delete(AutorModel autorModel) {
            try {
                var autor = Autores.FirstOrDefault(x => x.Id == autorModel.Id);
                Autores.Remove(autor);
                return RedirectToAction(nameof(Index));
            }
            catch {
                return View();
            }
        }
    }
}
