# CLAUDE.md - Development Guide

## Commands
- Build/Run: `npm run gen-prs` - Generates pull requests
- Test: No official test framework implemented (placeholder in package.json)
- TypeCheck: `npx tsc --noEmit` - Validates TypeScript types without emitting files

## Code Style
- **TypeScript**: Use strict mode with ES2020 target
- **Imports**: ES modules (`import`/`export`)
- **Formatting**:
  - No official formatter, but follow existing code patterns
  - Use 2-space indentation
- **Naming**:
  - camelCase for variables, functions, methods
  - PascalCase for interfaces, types, classes
  - Descriptive names that reflect purpose
- **Types**: 
  - Define interfaces for complex objects
  - Avoid `any` type, use proper typing
- **Functions**: Prefer arrow functions for consistency
- **Error Handling**: Use async/await with try/catch blocks

## Project Structure
- Source code in `/src` directory
- Entry point: `index.ts`
- TypeScript configuration in `tsconfig.json`
- Package uses `execa` for process execution and `faker` for test data generation