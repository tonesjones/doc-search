---
title: "Dart Support"
source_url: "https://docs.blackduck.com/r/detect/11.5.1/black-duck-detect/dart-support.html"
content_id: "aDPsNbAnUmZSRzrHPnvrCw"
version: "11.5.1"
section: "Package Manager information for Detect"
scraped_at: "2026-08-08T23:44:53.297008+00:00"
---

# Dart Support

## Related properties

Detector properties

## Overview

Detect has two detectors for Dart:

- Dart CLI detector
- Dart PubSpec Lock detector

Both detectors will run if they find the following files:

- pubspec.yaml
- pubspeck.lock

If Detect cannot find a pubspec.lock file, but it finds a pubspec.yaml file, it will prompt the user to run the 'pub get' command to generate the pubspec.lock file, and then run Detect again.

Both detectors parse the pubspec.yaml file to determine project name and version information.

The Dart PubSpec Lock detector parses the pubspec.lock file for dependency information. Since the file does not indicate relationships between components, results from this detector will be less accurate than those from the Dart CLI detector.

The Dart CLI detector runs the command 'pub deps' (which requires a pubspec.lock file to be present), and then parses the command's output for dependency information. The detector will first try to run the command using a dart executable (if found), but if it is unsuccessful because the target project requires the Flutter SDK then it will try using a flutter executable (if found).

You may specify the location of dart and flutter executables using the detect.dart.path and detect.flutter.path properties, respectively.

If you wish to exclude dev dependencies, you may do so using the detect.pub.dependency.types.excluded property, which will cause the detector to pass the --no-dev option when running 'pub deps'.
