theasder.github.io
==================

Site for vk.com/proglib page.

If you want to try scripts, you need to have OS X and MacDown preinstalled. You need to open `.bashrc` file and add certain code:

    alias write="python3 `full_path_to_script.py`"
    alias post="sh `full_path_to_post.sh`"
    
To write post, write this in command line:

    write `name_of_file` -name `name_of_note` -tags `some_tags` -cat `category_for_article`

To publish post, write this in command line:
    
    post
    
