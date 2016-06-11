import java.util.ArrayList;
/**
 * 
 * @author Christian Seely
 *
 */
public class Problem_Three {
	public static void main(String[] args) {
		  long max = 0;
		  long n = 600851475143L;
		  ArrayList<Long> primeFactors = new ArrayList<>();
		  long testDivisor = 2;
		  boolean terminate = false;
		  long remainder = 0;
		  //Find all prime factors of n.
		  while(!terminate)
		  {
		    if((testDivisor*testDivisor) > n)
		    {
		      if(n != 1)
		      {
		    	primeFactors.add(n);
		        terminate = true;
		      }
		      else
		      {
		    	 terminate = true;
		      }
		    }
		    if(n%testDivisor == 0 && !terminate)
		    {
		      primeFactors.add(testDivisor);
		      remainder = n%testDivisor;
		      n /= testDivisor;
		      if(remainder != 0)++testDivisor;
		      while(n%testDivisor == 0 &&!terminate) n /= testDivisor;
		    }
		    ++testDivisor;
		  }	  
		  //Find largest prime factor in primeFactors.
		  for(long pf: primeFactors)
		  {
			  if(pf>max)max=pf;
		  }
		  System.out.println(max);
	}
}
