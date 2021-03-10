# General Notes
## Object Oriented Programming
### Design Patterns
#### https://www.oodesign.com/
* Singleton
* Factory
* Abstract Factory
* Builder

## Setting up gmail mail forwarding with a google domain that is has a custom name server pointed at github pages (or something like that)
Oh man, so this was confusing. I had a google domain for my website, but I wanted to host it at github pages because it's free, and rather easy to setup. So in order to do this, I had to set up custom DNS on my google domain, which thereby disabled me from using the build in g suite stuff. In order to use the mail forwarding option, I found this link https://support.google.com/domains/answer/9428703 which showed me how to set up email forwarding to gmail with custom name servers. So I went to github to add the MX records to my DNS host (github), but there was nowhere to do that. Turns out I was actually using cloudflare (it's been awhile) for... I actually don't know exactly why (so I'll need to figure that out), but that is where I had my DNS info. There I was able to add the MX records. Then I was able to go into my google domains page, click the domain, click email in the left column, and add an email for mail forwarding. And it worked!

But it wasn't over yet! That was just for mail forwarding. To reply as that email, there was one more step! Followed this link: https://support.google.com/domains/answer/9437157. For Step 1.3, had to follow the two step verification process. For 2.8., make sure you change it from your smtp.<yourdomain>.com to smtp.gmail.com. For 2.10, the username is your gmail account your logged into. That's all, then it should work!
