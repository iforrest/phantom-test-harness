# phantom-test-harness
Test harness for a more pleasurable app building experience. Include a dummy BaseConnector, phantom.app, phantom.ph_utils, Vault, and ActionResult module. Each module has been optimized to best of my ability for test and debug.

# Why use this?
This test harness decouples Phantom App development from the Phantom platform. This means you can develop and test new and existing apps on your own machine withouth having to worry about all the Phantom dependencies. Yes, that means you can put "print" statements all over your code again, like a true Python programmer :)

It is important to note, that while this is a handy tool for app development it does not connect to phantom or test any phantom platform code, to that's still important.

# Logging
Activity will be logged to a file and to the console by default. The log file location is the current location of execution, unless otherwise specified (BaseConnector - log_path). Console logging can be disabled as well (BaseConnector - log_to_console)

# How to use
Clone this repo

Add the location of this project to your PYTHONPATH

export PYTHONPATH=$PYTHONPATH:/your/new/location/phantom-test-harness

Make sure you run your python code that tests your app from somewhere that you can import your app module from. I recommend just testing from withing your app code directory.

Check /examples for examples on how to use this.

That's it! Then start testing your code. Check the examples folder for a few ideas.

# Options

There are a lot of options that you can use depending on your scenario. Some options are strictly for debugging purposes, and some are for making sure that your app doesn't break. Options are defined in BaseConnector.py:init(). There are comments as to which each are for. Some probably need more clarity. Please see examples for some ideas of how to use and access these.

# Examples
Examples of usage can be found in /examples

# Other important stuff

This is very alpha. If you run into BaseConnector methods, or other things that haven't been implemented, please feel free to let me know, or contribute. Happy coding!
