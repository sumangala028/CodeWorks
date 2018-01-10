public class pattern{

	public static void main(String [] args) {

		for(int i =0; i < 4; i++)
		{
			for(int j=0; j<4-i; j++)
				System.out.print(" ");
			for(int k = 0; k <= 0; k++)
				System.out.print("o");
			for(int x =0 ; x <= i; x++)
				System.out.print("  ");
			for(int k = 0; k <= 0; k++)
				System.out.print("o");

			System.out.println();}

		for(int i =4; i > 0; i--){

			for(int j=0; j< 4-i; j++)
				System.out.print(" ");
			for(int k = 0; k <= 0; k++)
				System.out.print("o");
			for(int x =0 ; x <= i; x++)
				System.out.print("  ");
			for(int k = 0; k <= 0; k++)
				System.out.print("o");

			System.out.println();
		}
	}
}