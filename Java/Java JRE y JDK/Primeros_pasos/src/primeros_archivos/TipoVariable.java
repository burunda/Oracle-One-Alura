package primeros_archivos;

public class TipoVariable {
	
	public static void main(String[] args) {
		System.out.println("Hola gente!!!");
		
		int edad=36;
		System.out.println("Mi edad es " + edad);
		
		double salario=1250.56;
		System.out.println("y mi salario es " + salario);
		
		double variable1=230.89;
		int variable1Entero=(int) variable1;
		System.out.println("el float es " + variable1 + " y la convierte en entero en este " + variable1Entero);
		 
		long largo=1225641321684765413L;
		System.out.println("La variable long se utiliza para números enteros de hasta 20 digitos y se debe especificar con <<L>> al final para que lo reconozca el sistema, por ejemplo " + largo);
		short peque=12345;
		System.out.println("La variable short es para números enteros de hasta 5 digitos, por ejemplo "+ peque);
		byte masPeque=123;
		System.out.println("La variable byte es para números enteros de hasta 3 digitos, por ejemplo " + masPeque);
		float decimal=2.1512345F;
		System.out.println("La variable float es para números con hasta 7 decimales y debe especificar <<F>> al final para que lo reconozca el sistema, por ejemplo " + decimal);
		
	}

}
