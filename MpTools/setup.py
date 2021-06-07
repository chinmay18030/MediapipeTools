from distutils.core import setup

setup(
  name = 'MediaPipeTools',         # How you named your package folder (MyLib)
  packages = ['MediaPipeTools'],   # Chose the same as "name"
  version = '0.12',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'This package will help you use mediapipe tools easily',
  long_description="Mediapipe tools to use mediapipe library easily. Provides had tracking, face mesh and pose tracking. For more info see the repository https://github.com/chinmay18030/MediapipeTools",
  author = 'Ace Tech Academy',                   # Type in your name
  author_email = 'aceteachacademy@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/user/reponame',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',    # I explain this later on
  keywords = ['Mediapipe Tools', 'FaceMesh', 'hand tracking','pose tracking'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'opencv-python',
          'mediapipe',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3.6',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)