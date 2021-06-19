CREATE TABLE Autor(
	Id INT NOT NULL IDENTITY(1,1) PRIMARY KEY,
	Nome NVARCHAR(50),
	UltimoNome NVARCHAR(50),
	Nacionalidade NVARCHAR(50),
	QuantidadeLivrosPublicados INT,
	Nascimento DATETIME2,
);

DROP TABLE Autor;

SELECT * FROM Autor;

INSERT INTO Autor
	(Nome, UltimoNome, Nacionalidade, QuantidadeLivrosPublicados, Nascimento)
	VALUES('Tao', 'Hansen', 'Brasileiro', 5, '1996-01-31');

INSERT INTO Autor
(Nome, UltimoNome, Nacionalidade, QuantidadeLivrosPublicados, Nascimento)
VALUES('Tao', 'Hansen', 'Brasileiro', 5, '1996-01-31');

UPDATE Autor
	SET UltimoNome = 'Alterado'
	WHERE Id = 2;

DELETE FROM Autor WHERE Id = 2;

UPDATE Autor
SET Nome = 'taoe', UltimoNome = 'taoe', Nacionalidade = 'taoe', 
    QuantidadeLivrosPublicados = 1, Nascimento = '1996-01-31'
	WHERE Id = 1;