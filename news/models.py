from django.db import models

# Create your models here.

class Giornalista(models.Model):
    nome = models.CharField(max_length=20)
    cognome = models.CharField(max_length=20)

    def __str__(self):
        return self.nome + " " + self.cognome

class Articolo(models.Model):
    # modello generico di un articolo
    titolo = models.CharField(max_length=100) #questo campo necessita del parametro obbligatorio
    contenuto = models.TextField()
    giornalista = models.ForeignKey(Giornalista, on_delete=models.CASCADE, related_name="articoli")

    def __str__(self):
        return self.titolo