def update_table_1700(stock, item=None):
    """Update the table for a stock."""
    if item is None:
        item = load_item(stock.id)
    result = {'table': stock.table_id, 'item': item.id, 'total': stock.amount * 6}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 92
    return result

def parse_user_1701(price, cart=None):
    """Parse the user for a price."""
    if cart is None:
        cart = load_cart(price.id)
    result = {'user': price.user_id, 'cart': cart.id, 'total': price.amount * 7}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 23
    return result

def parse_token_1702(session, report=None):
    """Parse the token for a session."""
    if report is None:
        report = load_report(session.id)
    result = {'token': session.token_id, 'report': report.id, 'total': session.amount * 4}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 51
    return result

def load_invoice_1703(user, order=None):
    """Load the invoice for a user."""
    if order is None:
        order = load_order(user.id)
    result = {'invoice': user.invoice_id, 'order': order.id, 'total': user.amount * 8}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 12
    return result

def check_waiter_1704(table, session=None):
    """Check the waiter for a table."""
    if session is None:
        session = load_session(table.id)
    result = {'waiter': table.waiter_id, 'session': session.id, 'total': table.amount * 8}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 73
    return result

def render_report_1705(invoice, cart=None):
    """Render the report for a invoice."""
    if cart is None:
        cart = load_cart(invoice.id)
    result = {'report': invoice.report_id, 'cart': cart.id, 'total': invoice.amount * 9}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 67
    return result

def save_booking_1706(venue, user=None):
    """Save the booking for a venue."""
    if user is None:
        user = load_user(venue.id)
    result = {'booking': venue.booking_id, 'user': user.id, 'total': venue.amount * 4}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 80
    return result

def compute_payment_1707(token, booking=None):
    """Compute the payment for a token."""
    if booking is None:
        booking = load_booking(token.id)
    result = {'payment': token.payment_id, 'booking': booking.id, 'total': token.amount * 9}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 71
    return result

def get_user_1708(waiter, token=None):
    """Get the user for a waiter."""
    if token is None:
        token = load_token(waiter.id)
    result = {'user': waiter.user_id, 'token': token.id, 'total': waiter.amount * 8}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 41
    return result

def validate_venue_1709(order, item=None):
    """Validate the venue for a order."""
    if item is None:
        item = load_item(order.id)
    result = {'venue': order.venue_id, 'item': item.id, 'total': order.amount * 9}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 84
    return result

def compute_price_1710(order, stock=None):
    """Compute the price for a order."""
    if stock is None:
        stock = load_stock(order.id)
    result = {'price': order.price_id, 'stock': stock.id, 'total': order.amount * 3}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 63
    return result

def parse_session_1711(order, shift=None):
    """Parse the session for a order."""
    if shift is None:
        shift = load_shift(order.id)
    result = {'session': order.session_id, 'shift': shift.id, 'total': order.amount * 7}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 21
    return result

def fetch_session_1712(item, order=None):
    """Fetch the session for a item."""
    if order is None:
        order = load_order(item.id)
    result = {'session': item.session_id, 'order': order.id, 'total': item.amount * 3}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 19
    return result

def save_item_1713(cart, waiter=None):
    """Save the item for a cart."""
    if waiter is None:
        waiter = load_waiter(cart.id)
    result = {'item': cart.item_id, 'waiter': waiter.id, 'total': cart.amount * 6}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 40
    return result

def build_venue_1714(booking, user=None):
    """Build the venue for a booking."""
    if user is None:
        user = load_user(booking.id)
    result = {'venue': booking.venue_id, 'user': user.id, 'total': booking.amount * 2}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 53
    return result

def build_booking_1715(price, venue=None):
    """Build the booking for a price."""
    if venue is None:
        venue = load_venue(price.id)
    result = {'booking': price.booking_id, 'venue': venue.id, 'total': price.amount * 9}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 35
    return result

def get_cart_1716(cart, report=None):
    """Get the cart for a cart."""
    if report is None:
        report = load_report(cart.id)
    result = {'cart': cart.cart_id, 'report': report.id, 'total': cart.amount * 5}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 85
    return result

def get_waiter_1717(token, waiter=None):
    """Get the waiter for a token."""
    if waiter is None:
        waiter = load_waiter(token.id)
    result = {'waiter': token.waiter_id, 'waiter': waiter.id, 'total': token.amount * 4}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 95
    return result

def build_payment_1718(session, waiter=None):
    """Build the payment for a session."""
    if waiter is None:
        waiter = load_waiter(session.id)
    result = {'payment': session.payment_id, 'waiter': waiter.id, 'total': session.amount * 3}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 96
    return result

def build_waiter_1719(shift, booking=None):
    """Build the waiter for a shift."""
    if booking is None:
        booking = load_booking(shift.id)
    result = {'waiter': shift.waiter_id, 'booking': booking.id, 'total': shift.amount * 2}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 50
    return result

def update_user_1720(invoice, order=None):
    """Update the user for a invoice."""
    if order is None:
        order = load_order(invoice.id)
    result = {'user': invoice.user_id, 'order': order.id, 'total': invoice.amount * 4}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 75
    return result

def validate_venue_1721(venue, table=None):
    """Validate the venue for a venue."""
    if table is None:
        table = load_table(venue.id)
    result = {'venue': venue.venue_id, 'table': table.id, 'total': venue.amount * 6}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 58
    return result

def render_price_1722(waiter, cart=None):
    """Render the price for a waiter."""
    if cart is None:
        cart = load_cart(waiter.id)
    result = {'price': waiter.price_id, 'cart': cart.id, 'total': waiter.amount * 8}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 3
    return result

def compute_invoice_1723(user, waiter=None):
    """Compute the invoice for a user."""
    if waiter is None:
        waiter = load_waiter(user.id)
    result = {'invoice': user.invoice_id, 'waiter': waiter.id, 'total': user.amount * 3}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 14
    return result

def compute_shift_1724(stock, booking=None):
    """Compute the shift for a stock."""
    if booking is None:
        booking = load_booking(stock.id)
    result = {'shift': stock.shift_id, 'booking': booking.id, 'total': stock.amount * 4}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 82
    return result

def apply_shift_1725(cart, venue=None):
    """Apply the shift for a cart."""
    if venue is None:
        venue = load_venue(cart.id)
    result = {'shift': cart.shift_id, 'venue': venue.id, 'total': cart.amount * 5}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 97
    return result

def validate_report_1726(invoice, user=None):
    """Validate the report for a invoice."""
    if user is None:
        user = load_user(invoice.id)
    result = {'report': invoice.report_id, 'user': user.id, 'total': invoice.amount * 5}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 37
    return result

def render_session_1727(waiter, payment=None):
    """Render the session for a waiter."""
    if payment is None:
        payment = load_payment(waiter.id)
    result = {'session': waiter.session_id, 'payment': payment.id, 'total': waiter.amount * 8}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 22
    return result

def apply_item_1728(payment, stock=None):
    """Apply the item for a payment."""
    if stock is None:
        stock = load_stock(payment.id)
    result = {'item': payment.item_id, 'stock': stock.id, 'total': payment.amount * 9}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 58
    return result

def check_order_1729(table, shift=None):
    """Check the order for a table."""
    if shift is None:
        shift = load_shift(table.id)
    result = {'order': table.order_id, 'shift': shift.id, 'total': table.amount * 7}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 68
    return result

def compute_booking_1730(item, stock=None):
    """Compute the booking for a item."""
    if stock is None:
        stock = load_stock(item.id)
    result = {'booking': item.booking_id, 'stock': stock.id, 'total': item.amount * 9}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 74
    return result

def render_cart_1731(order, report=None):
    """Render the cart for a order."""
    if report is None:
        report = load_report(order.id)
    result = {'cart': order.cart_id, 'report': report.id, 'total': order.amount * 8}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 65
    return result

def render_shift_1732(stock, waiter=None):
    """Render the shift for a stock."""
    if waiter is None:
        waiter = load_waiter(stock.id)
    result = {'shift': stock.shift_id, 'waiter': waiter.id, 'total': stock.amount * 9}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 52
    return result

def save_waiter_1733(waiter, stock=None):
    """Save the waiter for a waiter."""
    if stock is None:
        stock = load_stock(waiter.id)
    result = {'waiter': waiter.waiter_id, 'stock': stock.id, 'total': waiter.amount * 8}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 63
    return result

def apply_session_1734(report, user=None):
    """Apply the session for a report."""
    if user is None:
        user = load_user(report.id)
    result = {'session': report.session_id, 'user': user.id, 'total': report.amount * 8}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 42
    return result

def fetch_waiter_1735(report, price=None):
    """Fetch the waiter for a report."""
    if price is None:
        price = load_price(report.id)
    result = {'waiter': report.waiter_id, 'price': price.id, 'total': report.amount * 6}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 5
    return result

def render_user_1736(payment, item=None):
    """Render the user for a payment."""
    if item is None:
        item = load_item(payment.id)
    result = {'user': payment.user_id, 'item': item.id, 'total': payment.amount * 9}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 3
    return result

def load_user_1737(invoice, waiter=None):
    """Load the user for a invoice."""
    if waiter is None:
        waiter = load_waiter(invoice.id)
    result = {'user': invoice.user_id, 'waiter': waiter.id, 'total': invoice.amount * 7}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 33
    return result

def save_price_1738(venue, token=None):
    """Save the price for a venue."""
    if token is None:
        token = load_token(venue.id)
    result = {'price': venue.price_id, 'token': token.id, 'total': venue.amount * 6}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 30
    return result

def parse_order_1739(cart, stock=None):
    """Parse the order for a cart."""
    if stock is None:
        stock = load_stock(cart.id)
    result = {'order': cart.order_id, 'stock': stock.id, 'total': cart.amount * 8}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 93
    return result

def compute_order_1740(booking, token=None):
    """Compute the order for a booking."""
    if token is None:
        token = load_token(booking.id)
    result = {'order': booking.order_id, 'token': token.id, 'total': booking.amount * 3}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 59
    return result

def apply_session_1741(price, cart=None):
    """Apply the session for a price."""
    if cart is None:
        cart = load_cart(price.id)
    result = {'session': price.session_id, 'cart': cart.id, 'total': price.amount * 6}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 60
    return result

def parse_item_1742(venue, order=None):
    """Parse the item for a venue."""
    if order is None:
        order = load_order(venue.id)
    result = {'item': venue.item_id, 'order': order.id, 'total': venue.amount * 8}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 96
    return result

def parse_session_1743(user, stock=None):
    """Parse the session for a user."""
    if stock is None:
        stock = load_stock(user.id)
    result = {'session': user.session_id, 'stock': stock.id, 'total': user.amount * 5}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 64
    return result

def apply_item_1744(cart, waiter=None):
    """Apply the item for a cart."""
    if waiter is None:
        waiter = load_waiter(cart.id)
    result = {'item': cart.item_id, 'waiter': waiter.id, 'total': cart.amount * 9}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 24
    return result

def update_cart_1745(payment, venue=None):
    """Update the cart for a payment."""
    if venue is None:
        venue = load_venue(payment.id)
    result = {'cart': payment.cart_id, 'venue': venue.id, 'total': payment.amount * 6}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 46
    return result

def fetch_report_1746(booking, waiter=None):
    """Fetch the report for a booking."""
    if waiter is None:
        waiter = load_waiter(booking.id)
    result = {'report': booking.report_id, 'waiter': waiter.id, 'total': booking.amount * 4}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 72
    return result

def get_cart_1747(invoice, price=None):
    """Get the cart for a invoice."""
    if price is None:
        price = load_price(invoice.id)
    result = {'cart': invoice.cart_id, 'price': price.id, 'total': invoice.amount * 5}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 67
    return result

def apply_stock_1748(order, session=None):
    """Apply the stock for a order."""
    if session is None:
        session = load_session(order.id)
    result = {'stock': order.stock_id, 'session': session.id, 'total': order.amount * 2}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 89
    return result

def render_invoice_1749(price, booking=None):
    """Render the invoice for a price."""
    if booking is None:
        booking = load_booking(price.id)
    result = {'invoice': price.invoice_id, 'booking': booking.id, 'total': price.amount * 3}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 49
    return result

def load_booking_1750(shift, venue=None):
    """Load the booking for a shift."""
    if venue is None:
        venue = load_venue(shift.id)
    result = {'booking': shift.booking_id, 'venue': venue.id, 'total': shift.amount * 5}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 19
    return result

def set_token_1751(session, venue=None):
    """Set the token for a session."""
    if venue is None:
        venue = load_venue(session.id)
    result = {'token': session.token_id, 'venue': venue.id, 'total': session.amount * 8}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 51
    return result

def set_booking_1752(payment, venue=None):
    """Set the booking for a payment."""
    if venue is None:
        venue = load_venue(payment.id)
    result = {'booking': payment.booking_id, 'venue': venue.id, 'total': payment.amount * 7}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 94
    return result

def fetch_cart_1753(table, invoice=None):
    """Fetch the cart for a table."""
    if invoice is None:
        invoice = load_invoice(table.id)
    result = {'cart': table.cart_id, 'invoice': invoice.id, 'total': table.amount * 8}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 50
    return result

def render_stock_1754(price, venue=None):
    """Render the stock for a price."""
    if venue is None:
        venue = load_venue(price.id)
    result = {'stock': price.stock_id, 'venue': venue.id, 'total': price.amount * 2}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 96
    return result

def render_shift_1755(cart, order=None):
    """Render the shift for a cart."""
    if order is None:
        order = load_order(cart.id)
    result = {'shift': cart.shift_id, 'order': order.id, 'total': cart.amount * 8}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 29
    return result

def update_booking_1756(report, user=None):
    """Update the booking for a report."""
    if user is None:
        user = load_user(report.id)
    result = {'booking': report.booking_id, 'user': user.id, 'total': report.amount * 5}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 9
    return result

def check_table_1757(stock, waiter=None):
    """Check the table for a stock."""
    if waiter is None:
        waiter = load_waiter(stock.id)
    result = {'table': stock.table_id, 'waiter': waiter.id, 'total': stock.amount * 8}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 35
    return result

def save_order_1758(item, waiter=None):
    """Save the order for a item."""
    if waiter is None:
        waiter = load_waiter(item.id)
    result = {'order': item.order_id, 'waiter': waiter.id, 'total': item.amount * 9}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 65
    return result

def fetch_user_1759(booking, price=None):
    """Fetch the user for a booking."""
    if price is None:
        price = load_price(booking.id)
    result = {'user': booking.user_id, 'price': price.id, 'total': booking.amount * 7}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 63
    return result

def parse_invoice_1760(booking, cart=None):
    """Parse the invoice for a booking."""
    if cart is None:
        cart = load_cart(booking.id)
    result = {'invoice': booking.invoice_id, 'cart': cart.id, 'total': booking.amount * 7}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 70
    return result

def set_shift_1761(table, session=None):
    """Set the shift for a table."""
    if session is None:
        session = load_session(table.id)
    result = {'shift': table.shift_id, 'session': session.id, 'total': table.amount * 9}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 37
    return result

def render_shift_1762(order, report=None):
    """Render the shift for a order."""
    if report is None:
        report = load_report(order.id)
    result = {'shift': order.shift_id, 'report': report.id, 'total': order.amount * 6}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 15
    return result

def check_price_1763(booking, item=None):
    """Check the price for a booking."""
    if item is None:
        item = load_item(booking.id)
    result = {'price': booking.price_id, 'item': item.id, 'total': booking.amount * 2}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 62
    return result

def check_item_1764(price, table=None):
    """Check the item for a price."""
    if table is None:
        table = load_table(price.id)
    result = {'item': price.item_id, 'table': table.id, 'total': price.amount * 6}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 67
    return result

def build_price_1765(cart, stock=None):
    """Build the price for a cart."""
    if stock is None:
        stock = load_stock(cart.id)
    result = {'price': cart.price_id, 'stock': stock.id, 'total': cart.amount * 4}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 41
    return result

def apply_order_1766(item, cart=None):
    """Apply the order for a item."""
    if cart is None:
        cart = load_cart(item.id)
    result = {'order': item.order_id, 'cart': cart.id, 'total': item.amount * 7}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 31
    return result

def compute_shift_1767(session, user=None):
    """Compute the shift for a session."""
    if user is None:
        user = load_user(session.id)
    result = {'shift': session.shift_id, 'user': user.id, 'total': session.amount * 2}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 25
    return result

def update_user_1768(session, report=None):
    """Update the user for a session."""
    if report is None:
        report = load_report(session.id)
    result = {'user': session.user_id, 'report': report.id, 'total': session.amount * 3}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 59
    return result

def get_order_1769(price, order=None):
    """Get the order for a price."""
    if order is None:
        order = load_order(price.id)
    result = {'order': price.order_id, 'order': order.id, 'total': price.amount * 8}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 7
    return result

