using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Infrastructure.Data.Repositories;
using Infrastructure.Data;

namespace Aula10Crud.Controllers {

     public class AutorController : Controller {
        private readonly AutorInMemoryRepository _autorRepository;

        public AutorController() {
            _autorRepository = new AutorInMemoryRepository();
        }

        // GET: AutorController
        public ActionResult Index() {
            return View();
        }

        // GET: AutorController/Details/5
        public ActionResult Details(int id) {
            var autor = _autorRepository.GetById(id);
            if (autor == null) {
                return RedirectToAction(nameof(Index));
            }
            else {
                return View(autor);
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
                _autorRepository.Create(autorModel);
                return RedirectToAction(nameof(Index));
            }
            catch {
                return View();
            }
        }

        // GET: AutorController/Edit/5
        public ActionResult Edit(int id) {
            var autor = _autorRepository.GetById(id);
            if (autor == null) {
                return RedirectToAction(nameof(Index));
            }
            else {
                return View(autor);
            }
        }

        // POST: AutorController/Edit/5
        [HttpPost]
        [ValidateAntiForgeryToken]
        public ActionResult Edit(AutorModel autorModel) {
            try {
                var autorEditado = _autorRepository.Edit(autorModel);
                if (autorEditado != null) {
                    return RedirectToAction(nameof(Details), new { id = autorEditado.Id });
                }
                else {
                    return RedirectToAction(nameof(Index));
                }
            }
            catch {
                return View();
            }
        }

        // GET: AutorController/Delete/5
        public ActionResult Delete(int id) {
            var autor = _autorRepository.GetById(id);
            if (autor == null) {
                return RedirectToAction(nameof(Index));
            }
            else {
                return View(autor);
            }
        }

        // POST: AutorController/Delete/5
        [HttpPost]
        [ValidateAntiForgeryToken]
        public ActionResult DeleteFromMemory(int id) {
            try {
                _autorRepository.Delete(id);
                return RedirectToAction(nameof(Index));
            }
            catch {
                return View();
            }
        }
    }
}
