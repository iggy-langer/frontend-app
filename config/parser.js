class Parser {
  /**
   * @param {string} input 
   */
  constructor(input) {
    this.input = input;
    this.index = 0;
  }

  /**
   * @returns {boolean}
   */
  hasNext() {
    return this.index < this.input.length;
  }

  /**
   * @returns {string}
   */
  nextToken() {
    let token = '';
    while (this.hasNext() && this.input[this.index].trim() !== '') {
      token += this.input[this.index];
      this.index++;
    }
    this.index++;
    return token.trim();
  }

  /**
   * @param {string} expected 
   * @throws {Error}
   * @returns {string}
   */
  expectToken(expected) {
    const token = this.nextToken();
    if (token !== expected) {
      throw new Error(`Expected token '${expected}', but got '${token}'`);
    }
    return token;
  }

  /**
   * @param {string} regex 
   * @returns {string|null}
   */
  match(regex) {
    const match = this.input.substring(this.index).match(regex);
    if (match) {
      this.index += match[0].length;
      return match[0];
    }
    return null;
  }
}

/**
 * @param {string} input 
 * @returns {Parser}
 */
function createParser(input) {
  return new Parser(input);
}

module.exports = { Parser, createParser };