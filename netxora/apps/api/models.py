from django.db import models

# Create your models here.
class Countries(models.Model):
    """Clase que representa la tabla de paises en la base de datos"""
    name = models.CharField(max_length=100, unique=True, verbose_name='Country Name')
    code = models.CharField(max_length=2, unique=True, verbose_name='Country Code')
    alpha2 = models.CharField(max_length=2, unique=True, verbose_name='Country Alpha2')
    alpha3 = models.CharField(max_length=3, primary_key=True, unique=True, verbose_name='Country Alpha3')
    flag = models.URLField(verbose_name='Flag URL')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created At')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated At')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'
        db_table = 'countries'
        ordering = ['name']

class States(models.Model):
    """Clase que representa la tabla de estados en la base de datos"""
    name = models.CharField(max_length=100, verbose_name='State Name')
    code = models.CharField(max_length=2, verbose_name='State Code')
    country = models.ForeignKey(Countries, on_delete=models.CASCADE, verbose_name='Country')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created At')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated At')

    def __str__(self):
        return f"{self.name} ({self.country.name})"
    
    class Meta:
        verbose_name = 'State'
        verbose_name_plural = 'States'
        db_table = 'states'
        ordering = ['name']
        unique_together = ('name', 'country')

class Cities(models.Model):
    """Clase que representa la tabla de ciudades en la base de datos"""
    name = models.CharField(max_length=100, verbose_name='City Name')
    state = models.ForeignKey(States, on_delete=models.CASCADE, verbose_name='State')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created At')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated At')

    def __str__(self):
        return f"{self.name} ({self.state.name})"
    
    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'
        db_table = 'cities'
        ordering = ['name']
        unique_together = ('name', 'state')

class Prefixes(models.Model):
    """Clase que representa la tabla de prefijos telefonicos en la base de datos"""
    name = models.CharField(max_length=100, verbose_name='Prefix Name')
    code = models.CharField(max_length=5, verbose_name='Prefix Code')
    country = models.ForeignKey(Countries, on_delete=models.CASCADE, verbose_name='Country')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created At')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated At')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Prefix'
        verbose_name_plural = 'Prefixes'
        db_table = 'prefixes'
        ordering = ['name']
        unique_together = ('code', 'country')

class Currency(models.Model):
    """Clase que representa la tabla de monedas en la base de datos"""
    name = models.CharField(max_length=100, verbose_name='Money Name')
    code = models.CharField(max_length=3, verbose_name='Money Code')
    symbol = models.CharField(max_length=5, verbose_name='Money Symbol')
    country = models.OneToOneField(Countries, on_delete=models.CASCADE, verbose_name='Country')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created At')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated At')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Currency'
        verbose_name_plural = 'Currencies'
        db_table = 'currencies'
        ordering = ['name']