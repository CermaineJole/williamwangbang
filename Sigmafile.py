public class PassiveBot
{
    public String greeting()
	{
		return "bro ts pmo jst strt askn u nt shkspr bru";
	}

    public String response(String statement){
        String resp = "";
        if(findKeyword(statement, ""

    }

    



    private int findKeyword(String statement, String goal, int startPos)
	{
	    String phrase = statement.trim();
	    int position = phrase.toLowerCase().indexOf(goal.toLowerCase(), startPos);
	    
	    while (position >= 0)
	    {
	        String before = " ";
	        String after = " ";
	        if (position > 0)
	        {
	            before = phrase.substring(position - 1, position).toLowerCase();
	        }
	        if (position + goal.length() < phrase.length())
	        {
	            after = phrase.substring(position + goal.length(),
	                                     position + goal.length() + 1).toLowerCase();
	        }
	        // uncomment to view the values of the variables
	        // System.out.println( " psn: " + position + " before: '" + before + "' after: '" + after + "'");
	        if (((before.compareTo ("a") < 0 ) || (before.compareTo("z") > 0)) &&
	            ((after.compareTo ("a") < 0 ) || (after.compareTo("z") > 0)))     
            {
                return position;
            }    
            position = phrase.indexOf(goal.toLowerCase(), position + 1);
	    }
	    return -1;
	}
	


}
