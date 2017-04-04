import java.util.*;
public class License_Key {
	
	public static String formatLicenseKey(String inputStr,int K){
		String output = "";
		
		//convert the string to upper case
		inputStr = inputStr.toUpperCase();
		
		/*replace all "-" with empty space and get the
		  size of the string without "-". Then calculate the size
		  of the first group so that all other groups are of 
		  size k*/
		inputStr = inputStr.replace("-", "");
		
		int size = inputStr.length();
		
		int first_group = size % K;
		int index = 0;
		
		/* Once the size of first group is computed place it in the 
		  output string then move to the next characters*/
		output += inputStr.substring(0, first_group);
		if(first_group > 0){
			output += "-";
		}
		
		index += first_group;
		
		/* Add remaining characters into output in the group of K size*/
		
		while(index < size){
			output += inputStr.substring(index, index+K);
			index += K;
			if(index < size-1)
				output += "-";
		}
		
		
		return output;
	}
	
	public static void main(String[] args){
		//Read input from the command prompt
		String inputStr = args[0];
		int K = Integer.parseInt(args[1]);
		
		System.out.println(formatLicenseKey(inputStr,K));
		
	}

}
