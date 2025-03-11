import { faker } from '@faker-js/faker';
import { $ } from 'execa';

const $$ = $({ stdio: 'inherit' });
const prTypes = ['feat', 'chore', 'fix', 'docs', 'perf', 'test'];
const teams = ['search', 'ci', 'cody'];

const randomInt = (max: number) => Math.floor(Math.random() * max);

function randomChoice<T>(elems: T[]): T {
  return elems[randomInt(elems.length)];
}

const range = (n: number) => Array.from(Array(n).keys());

const hackerPhrase = ({
  sentences = 1
}: {
  sentences?: number;
} = {}): string =>
  range(sentences)
    .map((_) => faker.hacker.phrase())
    .join(' ')
    .replace(/!/g, '.');

// Function to generate realistic-looking but fake API keys
const generateFakeApiKey = (): string => {
  const apiKeyPatterns = [
    // AWS-like key (20 chars)
    () => `AKIA${faker.string.alphanumeric(16).toUpperCase()}`,
    // Generic API key (40 chars with dashes)
    () =>
      Array(5)
        .fill(0)
        .map(() => faker.string.alphanumeric(8).toUpperCase())
        .join('-'),
    // JWT-like token
    () =>
      `eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.${faker.string.alphanumeric(
        32
      )}.${faker.string.alphanumeric(43)}`,
    // GitHub-like token
    () => `ghp_${faker.string.alphanumeric(36)}`,
    // Stripe-like key
    () =>
      `sk_${randomChoice(['test', 'live'])}_${faker.string.alphanumeric(24)}`,
    // Google API key-like
    () => `AIza${faker.string.alphanumeric(35)}`,
    // Firebase-like key
    () => `${faker.string.alphanumeric(28)}-${faker.string.alphanumeric(6)}`
  ];

  return randomChoice(apiKeyPatterns)();
};

// Function to generate random Python code with fake API keys
const generatePythonCode = (): string => {
  const imports = [
    'import requests',
    'import json',
    'import os',
    'from dotenv import load_dotenv',
    'import boto3',
    'import firebase_admin',
    'from google.cloud import storage',
    'import stripe'
  ];

  const selectedImports = range(randomInt(4) + 2)
    .map(() => randomChoice(imports))
    .filter((item, pos, self) => self.indexOf(item) === pos)
    .join('\n');

  const apiServices = [
    'aws',
    'stripe',
    'github',
    'firebase',
    'google',
    'azure',
    'twilio',
    'openai'
  ];

  const apiKeys: Record<string, string> = {};
  range(randomInt(3) + 1).forEach(() => {
    const service = randomChoice(apiServices);
    apiKeys[service] = generateFakeApiKey();
  });

  const apiKeysInCode = Object.entries(apiKeys)
    .map(([service, key]) => `${service.toUpperCase()}_API_KEY = "${key}"`)
    .join('\n');

  // Generate a simple Python class with the API keys
  const className = faker.hacker.noun().replace(/\s/g, '') + 'Client';
  const methodName = faker.hacker.verb().replace(/\s/g, '') + 'Data';

  return `${selectedImports}

# API Keys - For testing security tools only - These are fake keys
${apiKeysInCode}

class ${className}:
    def __init__(self):
        self.config = {
            "api_key": "${randomChoice(Object.values(apiKeys))}",
            "endpoint": "https://api.${faker.internet.domainName()}/v1/",
            "timeout": ${randomInt(10) + 5}
        }
    
    def ${methodName}(self, data_id=None):
        headers = {
            "Authorization": f"Bearer {self.config['api_key']}",
            "Content-Type": "application/json"
        }
        
        endpoint = f"{self.config['endpoint']}data/{data_id}" if data_id else f"{self.config['endpoint']}data"
        
        try:
            response = requests.get(endpoint, headers=headers, timeout=self.config['timeout'])
            return response.json()
        except Exception as e:
            print(f"Error fetching data: {e}")
            return None

# Example usage
if __name__ == "__main__":
    client = ${className}()
    result = client.${methodName}("${faker.string.uuid()}")
    print(json.dumps(result, indent=2))
`;
};

interface PR {
  type: string;
  branch: string;
  team: string;
  title: string;
  body: Body;
}

interface Body {
  description: string;
  changelog: string[];
}

function generatePR(): PR {
  return {
    type: randomChoice(prTypes),
    branch: `${faker.string
      .alpha({ length: 3 })
      .toLowerCase()}/${faker.git.branch()}`,
    team: randomChoice(teams),
    title: hackerPhrase(),
    body: {
      description: hackerPhrase({ sentences: 3 }),
      changelog: range(1 + randomInt(3)).map(() => hackerPhrase())
    }
  };
}

const prTitle = (pr: PR) => `${pr.type}/${pr.team}: ${pr.title}`;

const prBody = (pr: PR) => `${pr.body.description}

## Changelog:
${' - ' + pr.body.changelog.join('\n - ')}

NOTE: This PR contains fake API keys for testing security scanning tools.`;

async function main() {
  for (let i = 0; i < 1; i++) {
    const pr = generatePR();
    await $$`git checkout -b ${pr.branch}`;

    const pythonCode = generatePythonCode();
    const fileName = `test_${faker.lorem.slug({ min: 2, max: 4 })}.py`;

    await $`echo ${pythonCode}`.pipeStdout?.(`dummies/${fileName}`);
    await $$`git add dummies/*`;
    await $$`git commit -m ${prTitle(pr)}`;
    await $$`git push origin ${pr.branch}`;

    const { stdout: url } = await $`gh pr create --base main --title ${prTitle(
      pr
    )} --body ${prBody(pr)}`;

    console.log(url);
    // await $$`gh pr merge --squash ${url}`;
  }
}

main();
