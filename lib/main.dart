import 'package:english_words/english_words.dart';
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

enum LearningPace{ casual, standard, intensive }

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return ChangeNotifierProvider(
      create: (context) => MyAppState(),
      child: MaterialApp(
        title: 'Namer App',
        theme: ThemeData(
          useMaterial3: true,
          colorScheme: ColorScheme.fromSeed(seedColor: const Color.fromARGB(255, 34, 255, 45)),
        ),
        home: MyHomePage(),
      ),
    );
  }
}

class MyAppState extends ChangeNotifier {
  var current = WordPair.random();
  LearningPace? selectedPace;

  void setPace(LearningPace pace) {
    selectedPace = pace;
    notifyListeners();
  }
}

class MyHomePage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    //var appState = context.watch<MyAppState>();
    //var pair = appState.current;

    return Scaffold(
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            const Text(
              'Select your learning pace:', 
              style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold)
            ),
            const SizedBox(height: 20),
            PaceSelector(),
          ],
          ),
      ),
    );
  }
}

class PaceSelector extends StatelessWidget{
  @override
  Widget build(BuildContext context) {
    var appState = context.watch<MyAppState>();
    final theme = Theme.of(context);

    return Column(
      mainAxisAlignment: MainAxisAlignment.center,
      children: [
        PaceButton(
          pace: LearningPace.casual,
          label: 'Casual (5 min/day)',
          isSelected: appState.selectedPace == LearningPace.casual,
          onPressed: () => appState.setPace(LearningPace.casual),
          theme: theme,
        ),
        SizedBox(width: 10),
        PaceButton(
          pace: LearningPace.standard,
          label: 'Standard (15 min/day)',
          isSelected: appState.selectedPace == LearningPace.standard,
          onPressed: () => appState.setPace(LearningPace.standard),
          theme: theme,
          ),
          SizedBox(width: 10),
          PaceButton(
            pace: LearningPace.intensive,
            label: 'Intensive (30 min/day)',
            isSelected: appState.selectedPace == LearningPace.intensive,
            onPressed: () => appState.setPace(LearningPace.intensive),
            theme: theme,
            ),
      ],
    );
  }
}

class PaceButton extends StatelessWidget{
  final LearningPace pace;
  final String label;
  final bool isSelected;
  final VoidCallback onPressed;
  final ThemeData theme;

  const PaceButton({
    required this.pace,
    required this.label,
    required this.isSelected,
    required this.onPressed,
    required this.theme,
  });
  @override
  Widget build(BuildContext context) {
    return ElevatedButton(
      onPressed: onPressed,
      style: ElevatedButton.styleFrom(
        backgroundColor: isSelected
            ? theme.colorScheme.primary // Highlight selected button
            : theme.colorScheme.surface, // Default background
        foregroundColor: isSelected
            ? theme.colorScheme.onPrimary // Text/icon color for selected
            : theme.colorScheme.onSurface, // Default text/icon color
        padding: EdgeInsets.symmetric(horizontal: 16, vertical: 12),
        shape: RoundedRectangleBorder(
          borderRadius: BorderRadius.circular(8),
          side: BorderSide(
            color: isSelected ? theme.colorScheme.primary : theme.colorScheme.onSurface,
          ),
        ),
      ),
      child: Text(
        label,
        style: TextStyle(
          fontWeight: isSelected ? FontWeight.bold : FontWeight.normal,
        ),
      ),
    );
  }
}
