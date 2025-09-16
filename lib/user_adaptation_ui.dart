import 'package:flutter/material.dart';

class UserAdaptationUI extends StatelessWidget {
  const UserAdaptationUI({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text("User Adaptation UI")),
      body: const Center(
        child: Text("Aquí irá la adaptación de la interfaz ✨"),
      ),
    );
  }
}
