from distutils.core import setup
setup(
  name='tkstyles',         # How you named your package folder (MyLib)
  packages=['tkstyles'],   # Chose the same as "name"
  version='3.0.3',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description='A small library to apply basic styling to tkinter modules',   # Give a short description
  author = 'Kevin Lusignolo',                   # Type in your name
  author_email='kevinlusignolo@gmail.com',      # Type in your E-Mail
  url='https://github.com/klusignolo/tkstyles',   # Provide either the link to your github or to your website
  download_url='https://github.com/klusignolo/tkstyles/archive/v3.0.3.tar.gz',    # I explain this later on
  keywords=['tkinter', 'style', 'theme'],   # Keywords that define your package best
  classifiers=[
    'Development Status :: 5 - Production/Stable',      # Choose "3 - Alpha", "4 - Beta" or "5 - Production/Stable"
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.7',
  ],
)
