class User {
  constructor(name, industry) {
    this.name = name;
    this.industry = industry;
  }

  static getIndustries() {
    return [
      'Education',
      'Healthcare',
      'Finance',
      'Technology',
      'Retail',
    ];
  }
}

export { User }; 