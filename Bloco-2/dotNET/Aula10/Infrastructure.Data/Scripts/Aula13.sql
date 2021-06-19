SELECT * FROM Autor;

CREATE TABLE Livro(
	Id INT NOT NULL IDENTITY(1,1) PRIMARY KEY,
	Nome NVARCHAR(50) NOT NULL,
	AutorId INT NOT NULL FOREIGN KEY REFERENCES Autor(Id)
);

DROP TABLE Livro;

SELECT * FROM Livro;

INSERT INTO Livro
	(Nome, AutorId)
	VALUES('O despertar do amanhã', 1);

SELECT * FROM Livro
	INNER JOIN Autor
	ON Livro.AutorId = Autor.Id;

SELECT Livro.Nome, Autor.Nome, Autor.UltimoNome FROM Livro
	INNER JOIN Autor
	ON Livro.AutorId = Autor.Id;