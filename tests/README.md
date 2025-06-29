# Tests

This folder contains all testing files and test utilities.

## Structure

```
tests/
├── unit/              # Unit tests for individual functions/components
├── integration/       # Integration tests for API endpoints
├── e2e/              # End-to-end tests for user workflows
└── fixtures/         # Test data and mock responses
```

## Testing Strategy

### Frontend Testing
- Component unit tests
- UI interaction tests
- Visual regression tests
- Performance tests

### Backend Testing
- API endpoint tests
- Data model validation
- Integration tests with external APIs
- Load testing

### Test Data
- Mock NBA data for consistent testing
- Fixture files for different scenarios
- Sample API responses

## Running Tests

```bash
# Run all tests
npm test

# Run specific test suites
npm run test:unit
npm run test:integration
npm run test:e2e

# Watch mode for development
npm run test:watch
```

## Future Testing Tools

- Jest for JavaScript testing
- Pytest for Python scripts
- Cypress for E2E testing
- Testing Library for component testing
