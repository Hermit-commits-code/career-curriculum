# Topic: Python Immutability vs. TS Type Safety

**Date:** 2026-03-26
**Branch:** phase-1/foundations

## 🧠 Mental Model: The House & The Guard

- **Python (The House):** Integers are immutable. `x = 10` is a house. `x = 11` is a NEW house. The `id()` changes because we moved, we didn't renovate.
- **TypeScript (The Guard):** `any` is a fake ID. The compiler (Guard) lets the data in, but the program explodes at **Runtime** inside the factory.

## 🛠️ Technical Terms

- **Immutable:** Cannot be changed after creation.
- **Compile-time:** The "Sanitization" phase (Developer side).
- **Runtime:** The "Execution" phase (User side).
