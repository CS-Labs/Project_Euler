import java.util.ArrayList;
/**
 * 
 * @author Christian Seely
 *
 */
public class Problem_002 {

	public static int problemTwo()
	{
		int sum = 0;
		int prev = 0;
		int tmp;
		int curr = 1;
		int breakValue = 4_000_000;
		while(true) {
			tmp = curr;
			curr += prev;
			prev = tmp;
			if (curr > breakValue) break;
			if (curr % 2 == 0) sum += curr;
		}
		return sum;
	}

	public static void main(String[] args) { System.out.println(problemTwo()); }
	
}