import datetime;
import decimal;
import pyodbc;

#Se crea clase
class Estados:
    id: int = 0;
    
    #Metodos get-set del id
    def GetId(self) -> int:
        return self.id;

    def SetId(self, value: int) -> None:
        self.id = value;
    
    nombre: str = None;

    #Metodos get-set del nombre
    def GetNombre(self) -> str:
        return self.nombre;

    def SetNombre(self, value: str) -> None:
        self.nombre = value;

"""
    int(int-long)
    float, decimal, complex
    datetime (datetime.datetime.now())
    bool (True, False)
"""

#Conexion a la base de datos
class Conexion:
    cadena_conexion: str = """
                     Driver={MySQL ODBC 9.4 Unicode Driver};
                     Server=localhost;
                     Database=db_trabajo01;
                     PORT=3306;
                     user=user_trabajo01;
                     password=1234""";

    def CargarEstados(self) -> None:
        conexion = pyodbc.connect(self.cadena_conexion);

        consulta: str = """ SELECT * FROM estados; """;
        cursor = conexion.cursor();
        cursor.execute(consulta);

        lista: list = [];
        for elemento in cursor:
            entidad: Estados = Estados();
            entidad.SetId(elemento[0]);
            entidad.SetNombre(elemento[1]);
            lista.append(entidad);

        cursor.close();
        conexion.close();

        for estado in lista:
            print(str(estado.GetId()) + ", " + estado.GetNombre());

conexion = Conexion();
conexion.CargarEstados();
print("Conexión a base de datos MySQL");