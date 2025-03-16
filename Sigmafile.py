import java.util.Random;

public class PassiveBot {
    public String greeting() {
        return "Just ask away bru (say bye to end)";
    }

    public String response(String statement) {
        String resp = "";

        // Existing keyword checks
        if (findKeyword(statement, "help") >= 0 && findKeyword(statement, "with") >= 0) {
            resp = "But that is so easy";
        } else if (findKeyword(statement, "weather") >= 0) {
            resp = "Bro talkin bout weather say something better";
        } else if (findKeyword(statement, "who") >= 0 && findKeyword(statement, "you") >= 0) {
            resp = "I am the GOAT";
        }

        // New keyword checks and responses
        else if (findKeyword(statement, "hobby") >= 0) {
            resp = "I wish I had as much free time as you";
        } else if (findKeyword(statement, "choice") >= 0) {
            resp = "Oh, that's what you did..? Bold!";
        } else if (findKeyword(statement, "outfit") >= 0) {
            resp = "That looks... nice..";
        } else if (findKeyword(statement, "joke") >= 0) {
            resp = "It was funny, I just didn't laugh";
        } else if (findKeyword(statement, "listening") >= 0) {
            resp = "Oh, you were actually listening this time?";
        } else if (findKeyword(statement, "mistake") >= 0) {
            resp = "It's okay, nobody's perfect. Especially you";
        } else if (findKeyword(statement, "what") >= 0) {
            // More detailed response for "what"
            String afterWhat = getAfter(statement, "what");
            if (!afterWhat.isEmpty()) {
                resp = "Oh, you don't know what " + afterWhat + " is? How... unexpected.";
            } else {
                resp = "What? Oh, I'm sure you already know everything. Why even ask?";
            }
        }

        // Additional keywords and responses
        else if (findKeyword(statement, "why") >= 0) {
            resp = "Why? Oh, I don't know, maybe because the universe revolves around you?";
        } else if (findKeyword(statement, "how") >= 0) {
            resp = "How? Oh, I'm sure you'll figure it out eventually. Maybe.";
        } else if (findKeyword(statement, "when") >= 0) {
            resp = "When? Oh, I'm sure it'll happen *eventually*. Just be patient... or not.";
        } else if (findKeyword(statement, "where") >= 0) {
            resp = "Where? Oh, I'm sure you'll find it... if you actually try.";
        } else if (findKeyword(statement, "sorry") >= 0) {
            resp = "Sorry? Oh, I'm sure you *really* mean it this time.";
        } else if (findKeyword(statement, "happy") >= 0) {
            resp = "Happy? Oh, I'm sure your joy is just *infectious*.";
        } else if (findKeyword(statement, "sad") >= 0) {
            resp = "Sad? Oh, I'm sure the world is ending because of your *tragic* life.";
        } else if (findKeyword(statement, "stupid") >= 0) {
            resp = "Stupid? Oh, I'm sure you're an expert on the subject.";
        } else if (findKeyword(statement, "bored") >= 0) {
            resp = "Bored? Oh, I'm sure your life is just *so* hard. How do you cope?";
        } else if (findKeyword(statement, "love") >= 0) {
            resp = "Love? Oh, how adorable. I'm sure your relationship is *perfect*.";
        } else if (findKeyword(statement, "money") >= 0) {
            resp = "Money? Oh, I'm sure you're *rolling* in it. Must be nice.";
        } else if (findKeyword(statement, "work") >= 0) {
            resp = "Work? Wow, I'm sure your job is *so* much harder than everyone else's.";
        } else if (findKeyword(statement, "school") >= 0) {
            resp = "School? Oh, I'm sure you're just *thriving* in that environment.";
        } else if (findKeyword(statement, "family") >= 0) {
            resp = "Family? Oh, how original. Tell me more about your *fascinating* relatives.";
        }

        // Default response if no keyword is detected (randomly selected)
        else {
            resp = getRandomDefaultResponse();
        }

        return resp;
    }

    private int findKeyword(String statement, String goal, int startPos) {
        String phrase = statement.trim();
        int position = phrase.toLowerCase().indexOf(goal.toLowerCase(), startPos);

        while (position >= 0) {
            String before = " ";
            String after = " ";
            if (position > 0) {
                before = phrase.substring(position - 1, position).toLowerCase();
            }
            if (position + goal.length() < phrase.length()) {
                after = phrase.substring(position + goal.length(),
                        position + goal.length() + 1).toLowerCase();
            }
            if (((before.compareTo("a") < 0) || (before.compareTo("z") > 0)) &&
                    ((after.compareTo("a") < 0) || (after.compareTo("z") > 0))) {
                return position;
            }
            position = phrase.indexOf(goal.toLowerCase(), position + 1);
        }
        return -1;
    }

    private int findKeyword(String statement, String goal) {
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

    // Method to return a random default response
    private String getRandomDefaultResponse() {
        String[] defaultResponses = {
            "LEBROOOOOOOOOOOOOOOOOOOOOOOOOOON",
            "Oh, wow. Fascinating. Really.",
            "Yawn. Is this conversation over yet?",
            "Cool story. Tell it again, but this time with more enthusiasm.",
            "Oh, I see. You're one of those people who loves to hear themselves talk.",
            "Wow, such insight. I'm truly impressed. (Not really.)"
        };

        Random random = new Random();
        int index = random.nextInt(defaultResponses.length);
        return defaultResponses[index];
    }
}
