import java.util.ArrayList;
/**
 * 
 * @author Christian Seely
 *
 */
public class Problem_Two {
	public static void main(String[] args) {
	    int i = 1;
		int j = 2;
		int k = 0;
		int temp = 0;
		int sum = j;
		while(true)
		{
			k=i+j;
			if(k>4_000_000)break;
			if(k%2==0)sum+=k;
			temp = j;
			j = k;
			i = temp;
		}
		System.out.println(sum);
	}
	
}