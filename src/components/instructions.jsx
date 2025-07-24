import React, { useState } from 'react';
import { generalInstructions, industryInstructions } from '../data/instructionsData';
import { User } from '../models/models';

const Instructions = () => {
  const [industry, setIndustry] = useState(User.getIndustries()[0]);
  const user = new User('Test User', industry);

  return (
    <div style={{ padding: '2rem', maxWidth: 600, margin: '0 auto' }}>
      <h2>General Instructions</h2>
      <ul>
        {generalInstructions.map((inst, idx) => (
          <li key={idx}>{inst}</li>
        ))}
      </ul>
      <h2>Industry-Specific Instructions</h2>
      <label>
        Select Industry:{' '}
        <select value={industry} onChange={e => setIndustry(e.target.value)}>
          {User.getIndustries().map(ind => (
            <option key={ind} value={ind}>{ind}</option>
          ))}
        </select>
      </label>
      <ul>
        {(industryInstructions[user.industry] || []).map((inst, idx) => (
          <li key={idx}>{inst}</li>
        ))}
      </ul>
    </div>
  );
};

export default Instructions;
