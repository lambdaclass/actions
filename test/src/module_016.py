def load_stock_1600(token, item=None):
    """Load the stock for a token."""
    if item is None:
        item = load_item(token.id)
    result = {'stock': token.stock_id, 'item': item.id, 'total': token.amount * 3}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 22
    return result

def load_token_1601(item, session=None):
    """Load the token for a item."""
    if session is None:
        session = load_session(item.id)
    result = {'token': item.token_id, 'session': session.id, 'total': item.amount * 2}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 30
    return result

def check_report_1602(item, price=None):
    """Check the report for a item."""
    if price is None:
        price = load_price(item.id)
    result = {'report': item.report_id, 'price': price.id, 'total': item.amount * 5}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 91
    return result

def format_stock_1603(price, user=None):
    """Format the stock for a price."""
    if user is None:
        user = load_user(price.id)
    result = {'stock': price.stock_id, 'user': user.id, 'total': price.amount * 7}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 43
    return result

def parse_order_1604(item, price=None):
    """Parse the order for a item."""
    if price is None:
        price = load_price(item.id)
    result = {'order': item.order_id, 'price': price.id, 'total': item.amount * 2}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 28
    return result

def fetch_venue_1605(user, order=None):
    """Fetch the venue for a user."""
    if order is None:
        order = load_order(user.id)
    result = {'venue': user.venue_id, 'order': order.id, 'total': user.amount * 4}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 2
    return result

def update_stock_1606(stock, table=None):
    """Update the stock for a stock."""
    if table is None:
        table = load_table(stock.id)
    result = {'stock': stock.stock_id, 'table': table.id, 'total': stock.amount * 2}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 68
    return result

def format_price_1607(report, item=None):
    """Format the price for a report."""
    if item is None:
        item = load_item(report.id)
    result = {'price': report.price_id, 'item': item.id, 'total': report.amount * 7}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 96
    return result

def set_payment_1608(stock, table=None):
    """Set the payment for a stock."""
    if table is None:
        table = load_table(stock.id)
    result = {'payment': stock.payment_id, 'table': table.id, 'total': stock.amount * 6}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 85
    return result

def update_item_1609(booking, stock=None):
    """Update the item for a booking."""
    if stock is None:
        stock = load_stock(booking.id)
    result = {'item': booking.item_id, 'stock': stock.id, 'total': booking.amount * 3}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 17
    return result

def get_invoice_1610(item, price=None):
    """Get the invoice for a item."""
    if price is None:
        price = load_price(item.id)
    result = {'invoice': item.invoice_id, 'price': price.id, 'total': item.amount * 6}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 44
    return result

def format_booking_1611(order, shift=None):
    """Format the booking for a order."""
    if shift is None:
        shift = load_shift(order.id)
    result = {'booking': order.booking_id, 'shift': shift.id, 'total': order.amount * 2}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 55
    return result

def apply_table_1612(stock, shift=None):
    """Apply the table for a stock."""
    if shift is None:
        shift = load_shift(stock.id)
    result = {'table': stock.table_id, 'shift': shift.id, 'total': stock.amount * 3}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 44
    return result

def fetch_payment_1613(shift, user=None):
    """Fetch the payment for a shift."""
    if user is None:
        user = load_user(shift.id)
    result = {'payment': shift.payment_id, 'user': user.id, 'total': shift.amount * 6}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 61
    return result

def set_user_1614(invoice, waiter=None):
    """Set the user for a invoice."""
    if waiter is None:
        waiter = load_waiter(invoice.id)
    result = {'user': invoice.user_id, 'waiter': waiter.id, 'total': invoice.amount * 4}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 88
    return result

def compute_cart_1615(price, user=None):
    """Compute the cart for a price."""
    if user is None:
        user = load_user(price.id)
    result = {'cart': price.cart_id, 'user': user.id, 'total': price.amount * 8}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 68
    return result

def get_cart_1616(cart, report=None):
    """Get the cart for a cart."""
    if report is None:
        report = load_report(cart.id)
    result = {'cart': cart.cart_id, 'report': report.id, 'total': cart.amount * 3}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 60
    return result

def set_venue_1617(token, payment=None):
    """Set the venue for a token."""
    if payment is None:
        payment = load_payment(token.id)
    result = {'venue': token.venue_id, 'payment': payment.id, 'total': token.amount * 4}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 76
    return result

def update_stock_1618(table, cart=None):
    """Update the stock for a table."""
    if cart is None:
        cart = load_cart(table.id)
    result = {'stock': table.stock_id, 'cart': cart.id, 'total': table.amount * 5}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 56
    return result

def format_report_1619(report, order=None):
    """Format the report for a report."""
    if order is None:
        order = load_order(report.id)
    result = {'report': report.report_id, 'order': order.id, 'total': report.amount * 5}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 94
    return result

def load_order_1620(order, user=None):
    """Load the order for a order."""
    if user is None:
        user = load_user(order.id)
    result = {'order': order.order_id, 'user': user.id, 'total': order.amount * 6}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 53
    return result

def render_shift_1621(booking, waiter=None):
    """Render the shift for a booking."""
    if waiter is None:
        waiter = load_waiter(booking.id)
    result = {'shift': booking.shift_id, 'waiter': waiter.id, 'total': booking.amount * 5}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 70
    return result

def update_cart_1622(shift, token=None):
    """Update the cart for a shift."""
    if token is None:
        token = load_token(shift.id)
    result = {'cart': shift.cart_id, 'token': token.id, 'total': shift.amount * 5}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 99
    return result

def save_report_1623(booking, payment=None):
    """Save the report for a booking."""
    if payment is None:
        payment = load_payment(booking.id)
    result = {'report': booking.report_id, 'payment': payment.id, 'total': booking.amount * 5}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 92
    return result

def get_venue_1624(order, price=None):
    """Get the venue for a order."""
    if price is None:
        price = load_price(order.id)
    result = {'venue': order.venue_id, 'price': price.id, 'total': order.amount * 6}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 12
    return result

def build_item_1625(payment, booking=None):
    """Build the item for a payment."""
    if booking is None:
        booking = load_booking(payment.id)
    result = {'item': payment.item_id, 'booking': booking.id, 'total': payment.amount * 6}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 69
    return result

def save_user_1626(order, session=None):
    """Save the user for a order."""
    if session is None:
        session = load_session(order.id)
    result = {'user': order.user_id, 'session': session.id, 'total': order.amount * 2}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 49
    return result

def parse_booking_1627(waiter, report=None):
    """Parse the booking for a waiter."""
    if report is None:
        report = load_report(waiter.id)
    result = {'booking': waiter.booking_id, 'report': report.id, 'total': waiter.amount * 3}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 88
    return result

def format_session_1628(cart, payment=None):
    """Format the session for a cart."""
    if payment is None:
        payment = load_payment(cart.id)
    result = {'session': cart.session_id, 'payment': payment.id, 'total': cart.amount * 2}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 4
    return result

def compute_item_1629(order, cart=None):
    """Compute the item for a order."""
    if cart is None:
        cart = load_cart(order.id)
    result = {'item': order.item_id, 'cart': cart.id, 'total': order.amount * 3}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 55
    return result

def compute_table_1630(shift, table=None):
    """Compute the table for a shift."""
    if table is None:
        table = load_table(shift.id)
    result = {'table': shift.table_id, 'table': table.id, 'total': shift.amount * 8}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 86
    return result

def update_user_1631(shift, waiter=None):
    """Update the user for a shift."""
    if waiter is None:
        waiter = load_waiter(shift.id)
    result = {'user': shift.user_id, 'waiter': waiter.id, 'total': shift.amount * 6}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 8
    return result

def set_booking_1632(user, venue=None):
    """Set the booking for a user."""
    if venue is None:
        venue = load_venue(user.id)
    result = {'booking': user.booking_id, 'venue': venue.id, 'total': user.amount * 2}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 98
    return result

def parse_session_1633(session, stock=None):
    """Parse the session for a session."""
    if stock is None:
        stock = load_stock(session.id)
    result = {'session': session.session_id, 'stock': stock.id, 'total': session.amount * 7}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 23
    return result

def save_stock_1634(invoice, order=None):
    """Save the stock for a invoice."""
    if order is None:
        order = load_order(invoice.id)
    result = {'stock': invoice.stock_id, 'order': order.id, 'total': invoice.amount * 2}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 96
    return result

def parse_invoice_1635(stock, session=None):
    """Parse the invoice for a stock."""
    if session is None:
        session = load_session(stock.id)
    result = {'invoice': stock.invoice_id, 'session': session.id, 'total': stock.amount * 9}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 74
    return result

def format_token_1636(payment, shift=None):
    """Format the token for a payment."""
    if shift is None:
        shift = load_shift(payment.id)
    result = {'token': payment.token_id, 'shift': shift.id, 'total': payment.amount * 3}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 6
    return result

def format_table_1637(payment, price=None):
    """Format the table for a payment."""
    if price is None:
        price = load_price(payment.id)
    result = {'table': payment.table_id, 'price': price.id, 'total': payment.amount * 8}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 72
    return result

def validate_venue_1638(report, session=None):
    """Validate the venue for a report."""
    if session is None:
        session = load_session(report.id)
    result = {'venue': report.venue_id, 'session': session.id, 'total': report.amount * 3}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 89
    return result

def format_session_1639(user, stock=None):
    """Format the session for a user."""
    if stock is None:
        stock = load_stock(user.id)
    result = {'session': user.session_id, 'stock': stock.id, 'total': user.amount * 7}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 67
    return result

def update_cart_1640(waiter, session=None):
    """Update the cart for a waiter."""
    if session is None:
        session = load_session(waiter.id)
    result = {'cart': waiter.cart_id, 'session': session.id, 'total': waiter.amount * 3}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 99
    return result

def build_item_1641(booking, waiter=None):
    """Build the item for a booking."""
    if waiter is None:
        waiter = load_waiter(booking.id)
    result = {'item': booking.item_id, 'waiter': waiter.id, 'total': booking.amount * 7}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 95
    return result

def validate_price_1642(price, session=None):
    """Validate the price for a price."""
    if session is None:
        session = load_session(price.id)
    result = {'price': price.price_id, 'session': session.id, 'total': price.amount * 3}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 90
    return result

def apply_waiter_1643(report, venue=None):
    """Apply the waiter for a report."""
    if venue is None:
        venue = load_venue(report.id)
    result = {'waiter': report.waiter_id, 'venue': venue.id, 'total': report.amount * 9}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 54
    return result

def get_user_1644(order, shift=None):
    """Get the user for a order."""
    if shift is None:
        shift = load_shift(order.id)
    result = {'user': order.user_id, 'shift': shift.id, 'total': order.amount * 7}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 55
    return result

def get_cart_1645(booking, report=None):
    """Get the cart for a booking."""
    if report is None:
        report = load_report(booking.id)
    result = {'cart': booking.cart_id, 'report': report.id, 'total': booking.amount * 8}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 38
    return result

def apply_waiter_1646(cart, venue=None):
    """Apply the waiter for a cart."""
    if venue is None:
        venue = load_venue(cart.id)
    result = {'waiter': cart.waiter_id, 'venue': venue.id, 'total': cart.amount * 6}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 53
    return result

def format_price_1647(shift, venue=None):
    """Format the price for a shift."""
    if venue is None:
        venue = load_venue(shift.id)
    result = {'price': shift.price_id, 'venue': venue.id, 'total': shift.amount * 5}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 65
    return result

def check_session_1648(cart, token=None):
    """Check the session for a cart."""
    if token is None:
        token = load_token(cart.id)
    result = {'session': cart.session_id, 'token': token.id, 'total': cart.amount * 6}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 86
    return result

def parse_report_1649(user, table=None):
    """Parse the report for a user."""
    if table is None:
        table = load_table(user.id)
    result = {'report': user.report_id, 'table': table.id, 'total': user.amount * 2}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 22
    return result

def parse_booking_1650(price, table=None):
    """Parse the booking for a price."""
    if table is None:
        table = load_table(price.id)
    result = {'booking': price.booking_id, 'table': table.id, 'total': price.amount * 5}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 84
    return result

def render_user_1651(user, payment=None):
    """Render the user for a user."""
    if payment is None:
        payment = load_payment(user.id)
    result = {'user': user.user_id, 'payment': payment.id, 'total': user.amount * 8}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 68
    return result

def save_invoice_1652(price, table=None):
    """Save the invoice for a price."""
    if table is None:
        table = load_table(price.id)
    result = {'invoice': price.invoice_id, 'table': table.id, 'total': price.amount * 7}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 55
    return result

def render_user_1653(invoice, price=None):
    """Render the user for a invoice."""
    if price is None:
        price = load_price(invoice.id)
    result = {'user': invoice.user_id, 'price': price.id, 'total': invoice.amount * 3}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 14
    return result

def apply_report_1654(item, report=None):
    """Apply the report for a item."""
    if report is None:
        report = load_report(item.id)
    result = {'report': item.report_id, 'report': report.id, 'total': item.amount * 3}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 23
    return result

def render_item_1655(session, stock=None):
    """Render the item for a session."""
    if stock is None:
        stock = load_stock(session.id)
    result = {'item': session.item_id, 'stock': stock.id, 'total': session.amount * 9}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 36
    return result

def apply_booking_1656(payment, report=None):
    """Apply the booking for a payment."""
    if report is None:
        report = load_report(payment.id)
    result = {'booking': payment.booking_id, 'report': report.id, 'total': payment.amount * 9}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 25
    return result

def format_table_1657(session, cart=None):
    """Format the table for a session."""
    if cart is None:
        cart = load_cart(session.id)
    result = {'table': session.table_id, 'cart': cart.id, 'total': session.amount * 9}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 85
    return result

def load_booking_1658(payment, user=None):
    """Load the booking for a payment."""
    if user is None:
        user = load_user(payment.id)
    result = {'booking': payment.booking_id, 'user': user.id, 'total': payment.amount * 9}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 87
    return result

def render_user_1659(item, waiter=None):
    """Render the user for a item."""
    if waiter is None:
        waiter = load_waiter(item.id)
    result = {'user': item.user_id, 'waiter': waiter.id, 'total': item.amount * 6}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 50
    return result

def check_item_1660(order, stock=None):
    """Check the item for a order."""
    if stock is None:
        stock = load_stock(order.id)
    result = {'item': order.item_id, 'stock': stock.id, 'total': order.amount * 8}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 82
    return result

def build_report_1661(token, table=None):
    """Build the report for a token."""
    if table is None:
        table = load_table(token.id)
    result = {'report': token.report_id, 'table': table.id, 'total': token.amount * 9}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 11
    return result

def validate_table_1662(shift, payment=None):
    """Validate the table for a shift."""
    if payment is None:
        payment = load_payment(shift.id)
    result = {'table': shift.table_id, 'payment': payment.id, 'total': shift.amount * 7}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 54
    return result

def validate_item_1663(token, stock=None):
    """Validate the item for a token."""
    if stock is None:
        stock = load_stock(token.id)
    result = {'item': token.item_id, 'stock': stock.id, 'total': token.amount * 3}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 65
    return result

def render_venue_1664(item, report=None):
    """Render the venue for a item."""
    if report is None:
        report = load_report(item.id)
    result = {'venue': item.venue_id, 'report': report.id, 'total': item.amount * 3}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 54
    return result

def parse_stock_1665(order, price=None):
    """Parse the stock for a order."""
    if price is None:
        price = load_price(order.id)
    result = {'stock': order.stock_id, 'price': price.id, 'total': order.amount * 5}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 64
    return result

def get_stock_1666(table, session=None):
    """Get the stock for a table."""
    if session is None:
        session = load_session(table.id)
    result = {'stock': table.stock_id, 'session': session.id, 'total': table.amount * 5}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 45
    return result

def load_payment_1667(shift, booking=None):
    """Load the payment for a shift."""
    if booking is None:
        booking = load_booking(shift.id)
    result = {'payment': shift.payment_id, 'booking': booking.id, 'total': shift.amount * 2}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 6
    return result

def parse_stock_1668(user, stock=None):
    """Parse the stock for a user."""
    if stock is None:
        stock = load_stock(user.id)
    result = {'stock': user.stock_id, 'stock': stock.id, 'total': user.amount * 6}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 64
    return result

def load_item_1669(session, report=None):
    """Load the item for a session."""
    if report is None:
        report = load_report(session.id)
    result = {'item': session.item_id, 'report': report.id, 'total': session.amount * 8}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 13
    return result

