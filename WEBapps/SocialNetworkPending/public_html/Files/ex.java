public class ex{
public static void main(String[] args)
{
int[] a={1,10,50};
int len=a.length;
int max=0;
for(int k:a)
	{
	if(k>max)
		max=k;
	}
System.out.println(max);
}
}
