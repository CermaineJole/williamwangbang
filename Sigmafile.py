public class PassiveBot
{
    public String greeting()
	{
		return "bro ts pmo jst strt askn u nt shkspr bru";
	}

    public String response(String statement){
        String resp = "";
        if(findKeyword(statement, "poop"){
		resp = "i love poop";
	}

    }
    public String response(String statement){
        String resp = "";
        if(findKeyword(statement, "brush") >0 && (findKeyword(statement, "brushed") >0 && (findKeyword(statement, "teeth") >0 {
		resp = "wow good job remembering to brush your teeth, thats definitely a skill.";
	}

    }
    public String response(String statement){
        String resp = "";
        if(findKeyword(statement, "poop"){
		resp = "i love poop";
	}

    }
    public String response(String statement){
        String resp = "";
        if(findKeyword(statement, "poop"){
		resp = "i love poop";
	}

    }
    public String response(String statement){
        String resp = "";
        if(findKeyword(statement, "poop"){
		resp = "i love poop";
	}

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
	


}
