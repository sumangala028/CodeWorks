public class traingleNumbers{

	public static void main(String [] args) {

	int num = 0;
	int sum =0;

	for(int i =1; i <= 100; i++)
	{
		num += i;
		sum += num;
	}
	System.out.println("The sum is " + sum);


	}
}