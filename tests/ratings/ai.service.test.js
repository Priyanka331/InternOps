const {
  generateRatingSuggestion,
} = require('../../backend/src/modules/ratings/ai.service');

describe('generateRatingSuggestion', () => {
  it('returns valid score and reason when AI response is correct', async () => {
    const mockData = {
      user: { id: '123', role: 'intern' },
      metrics: { attendancePercentage: 90, verificationRate: 80 },
    };
    const result = await generateRatingSuggestion(mockData);
    expect(result.source).toBe('ai');
    expect(result.suggestedScore).toBeGreaterThanOrEqual(1);
    expect(result.suggestedScore).toBeLessThanOrEqual(10);
    expect(result.reasoning.length).toBeGreaterThan(0);
  });

  it('handles invalid JSON gracefully', async () => {
    const badData = { user: { id: 'bad' }, metrics: {} };
    const result = await generateRatingSuggestion(badData);
    expect(
      result.suggestedScore === null ||
        typeof result.suggestedScore === 'number'
    ).toBe(true);
  });
});
