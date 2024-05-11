# Super Simple Kivy Buildozer Example

This just works. Easy peasy. Kivy and Buildozer are pretty neat!

# To run

```bash
git clone {this repo}
cd super_simple_kivy_buildozer_example
python -m venv .venv
python -m pip install -r requirements.txt
export PATH=$PATH:~/.local/bin/
buildozer -v android debug
```

And the the apk will be in `bin/`. Copy it to your phone however you like and install =]

# Make your app do this

Just do these things:

- Follow [the buildozer docs](https://buildozer.readthedocs.io/en/latest/). They're very simple!
- Run `buildozer init` in your project
- Have a main.py that starts a kivy app
- Run `buildozer android debug`

# Where'd you get that great png?

Oh man, check out [OMG-IMG](https://icons8.com/license). They got tons of great stuff!
