public class PassiveBot
{
    public String greeting()
	{
		return "bro ts pmo jst strt askn u nt shkspr bru";
	}

    public String response(String statement){
        String resp = "";
        if(findKeyword(statement, "poop")>=0 && findKeyword(statement, "sigma")>=0){
		resp = "i love poop";
	}
	return resp;

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
	        if (((before.compareTo ("a") < 0 ) || (before.compareTo("z") > 0)) &&
	            ((after.compareTo ("a") < 0 ) || (after.compareTo("z") > 0)))     
            {
                return position;
            }    
            position = phrase.indexOf(goal.toLowerCase(), position + 1);
	    }
	    return -1;
	}


private int findKeyword(String statement, String goal)
	{
	    return findKeyword(statement, goal, 0);
	}

public String getAfter(String statement, String keyword) {
        int keywordPosition = findKeyword(statement, keyword);
        if (keywordPosition == -1) {
            return ""; // Keyword not found
        }

        // Find the start of the next word
        int nextWordStart = keywordPosition + keyword.length();
        while (nextWordStart < statement.length() && !Character.isLetter(statement.charAt(nextWordStart))) {
            nextWordStart++;
        }

        // Find the end of the next word
        int nextWordEnd = nextWordStart;
        while (nextWordEnd < statement.length() && Character.isLetter(statement.charAt(nextWordEnd))) {
            nextWordEnd++;
        }

        if (nextWordStart >= statement.length() || nextWordEnd <= nextWordStart) {
            return ""; // No word after the keyword
        }

        return statement.substring(nextWordStart, nextWordEnd);
    }
	


}
