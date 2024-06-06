from .okxclient import OkxClient
from .consts import *
import aiohttp

class AsyncMarketAPI(OkxClient):
    def __init__(self,
                 api_key='-1',
                 api_secret_key='-1',
                 passphrase='-1',
                 use_server_time=False,
                 flag='1',
                 domain='https://www.okx.com',
                 debug=True,
                 proxy=None):
        super().__init__(api_key, api_secret_key, passphrase, use_server_time, flag, domain, debug, proxy)



    async def _request_with_params(self, method, endpoint, params):
        url = f"{self.domain}{endpoint}"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.API_KEY}"
        }
        async with aiohttp.ClientSession() as session:
            async with session.request(method, url, params=params, headers=headers) as response:
                return await response.json()

    async def _request_without_params(self, method, endpoint):
        url = f"{self.domain}{endpoint}"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.API_KEY}"
        }
        async with aiohttp.ClientSession() as session:
            async with session.request(method, url, headers=headers) as response:
                return await response.json()

    async def get_tickers(self, instType, uly='', instFamily=''):
        params = {'instType': instType, 'uly': uly, 'instFamily': instFamily}
        return await self._request_with_params('GET', TICKERS_INFO, params)

    async def get_ticker(self, instId):
        params = {'instId': instId}
        return await self._request_with_params('GET', TICKER_INFO, params)

    async def get_index_tickers(self, quoteCcy='', instId=''):
        params = {'quoteCcy': quoteCcy, 'instId': instId}
        return await self._request_with_params('GET', INDEX_TICKERS, params)

    async def get_orderbook(self, instId, sz=''):
        params = {'instId': instId, 'sz': sz}
        return await self._request_with_params('GET', ORDER_BOOKS, params)

    async def get_candlesticks(self, instId, after='', before='', bar='', limit=''):
        params = {'instId': instId, 'after': after, 'before': before, 'bar': bar, 'limit': limit}
        return await self._request_with_params('GET', MARKET_CANDLES, params)

    async def get_history_candlesticks(self, instId, after='', before='', bar='', limit=''):
        params = {'instId': instId, 'after': after, 'before': before, 'bar': bar, 'limit': limit}
        return await self._request_with_params('GET', HISTORY_CANDLES, params)

    async def get_index_candlesticks(self, instId, after='', before='', bar='', limit=''):
        params = {'instId': instId, 'after': after, 'before': before, 'bar': bar, 'limit': limit}
        return await self._request_with_params('GET', INDEX_CANSLES, params)


    async def get_mark_price_candlesticks(self, instId, after='', before='', bar='', limit=''):
        params = {'instId': instId, 'after': after, 'before': before, 'bar': bar, 'limit': limit}
        return await self._request_with_params('GET', MARKPRICE_CANDLES, params)

    async def get_trades(self, instId, limit=''):
        params = {'instId': instId, 'limit': limit}
        return await self._request_with_params('GET', MARKET_TRADES, params)

    async def get_volume(self):
        return await self._request_without_params('GET', VOLUMNE)

    async def get_oracle(self):
        return await self._request_without_params('GET', ORACLE)

    async def get_tier(self, instType='', tdMode='', uly='', instId='', ccy='', tier=''):
        params = {'instType': instType, 'tdMode': tdMode, 'uly': uly, 'instId': instId, 'ccy': ccy, 'tier': tier}
        return await self._request_with_params('GET', TIER, params)

    async def get_index_components(self, index=''):
        params = {'index': index}
        return await self._request_with_params('GET', INDEX_COMPONENTS, params)

    async def get_exchange_rate(self):
        return await self._request_without_params('GET', EXCHANGE_RATE)

    async def get_history_trades(self, instId='', type='', after='', before='', limit=''):
        params = {'instId': instId, 'type': type, 'after': after, 'before': before, 'limit': limit}
        return await self._request_with_params('GET', HISTORY_TRADES, params)

    async def get_block_ticker(self, instId=''):
        params = {'instId': instId}
        return await self._request_with_params('GET', BLOCK_TICKER, params)

    async def get_block_tickers(self, instType='', uly='', instFamily=''):
        params = {'instType': instType, 'uly': uly, 'instFamily': instFamily}
        return await self._request_with_params('GET', BLOCK_TICKERS, params)

    async def get_block_trades(self, instId=''):
        params = {'instId': instId}
        return await self._request_with_params('GET', BLOCK_TRADES, params)

    async def get_order_lite_book(self, instId=''):
        params = {'instId': instId}
        return await self._request_with_params('GET', GET_ORDER_LITE_BOOK, params)

    async def get_option_trades(self, instFamily=''):
        params = {'instFamily': instFamily}
        return await self._request_with_params('GET', GET_OPTION_TRADES, params)
