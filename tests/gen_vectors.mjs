// Regenerate reference vectors: node tests/gen_vectors.mjs > tests/vectors.json
// Each case mirrors CASES in test_signature.py; expected values come from JSON.stringify + crypto, like the server.
import { createHmac } from 'crypto'

const SECRET = 'test-secret-key'
const WEBHOOK_SECRET = 'webhook-secret'
const TIMESTAMP = '20261106153045123'

const cases = {
  simple: { accountNumber: '0123456789', amount: 100000, content: 'Thanh toan don hang' },
  unicode: { name: 'Nguyễn Văn A', note: 'Cảm ơn 🙏' },
  escapes: { s: 'quote " backslash \\ slash / tab\t nl\n cr\r bs\b ff\f ctl\u0001 del\u007f <a>&\'' },
  line_separators: { s: '  ' },
  lone_surrogate: { s: 'a\ud800b' },
  floats: {
    a: 1.0, b: 0.1, c: 123.456, d: -2.5, e: 1e21, f: 1e-7, g: 1.5e-6, h: 100.0, i: 1e20, j: -0.0,
    k: 0.000001, l: 123456789.123, m: 5e-324, n: 1.7976931348623157e308, o: 0.1 + 0.2,
  },
  nested: { items: [{ id: 1, ok: true, v: null }, [], {}], meta: { x: [1, 2.0, '3'] } },
  empty: {},
  decimal: { amount: 1000.5 },
  enum_value: { bankName: 'ACB' },
  max_safe_int: { n: 9007199254740991 },
}

const sign = (secret, json) => createHmac('sha512', secret).update(`${TIMESTAMP}:${json}`).digest('hex')

const requests = {}
for (const [name, value] of Object.entries(cases)) {
  const json = JSON.stringify(value)
  requests[name] = { json, signature: sign(SECRET, json) }
}

const webhookBody = {
  clientId: 'cid', transactionCode: 'FT123', amount: 50000, content: 'Chuyển tiền', bank: 'ACB',
  accountNumber: '123', transactionDate: '20261106153000', additionalData: [{ name: 'k', value: 'v' }],
}
const webhookJson = JSON.stringify(webhookBody)

console.log(JSON.stringify({
  secret: SECRET,
  webhookSecret: WEBHOOK_SECRET,
  timestamp: TIMESTAMP,
  requests,
  webhook: { json: webhookJson, signature: sign(WEBHOOK_SECRET, webhookJson) },
  urlValidation: {
    plainToken: 'abc123',
    encryptedToken: createHmac('sha256', WEBHOOK_SECRET).update('abc123').digest('hex'),
  },
}, null, 2))
