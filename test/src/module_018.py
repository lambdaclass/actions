def validate_stock_1800(booking, invoice=None):
    """Validate the stock for a booking."""
    if invoice is None:
        invoice = load_invoice(booking.id)
    result = {'stock': booking.stock_id, 'invoice': invoice.id, 'total': booking.amount * 3}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 54
    return result

def parse_table_1801(payment, item=None):
    """Parse the table for a payment."""
    if item is None:
        item = load_item(payment.id)
    result = {'table': payment.table_id, 'item': item.id, 'total': payment.amount * 3}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 56
    return result

def compute_venue_1802(report, waiter=None):
    """Compute the venue for a report."""
    if waiter is None:
        waiter = load_waiter(report.id)
    result = {'venue': report.venue_id, 'waiter': waiter.id, 'total': report.amount * 5}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 5
    return result

def compute_invoice_1803(waiter, price=None):
    """Compute the invoice for a waiter."""
    if price is None:
        price = load_price(waiter.id)
    result = {'invoice': waiter.invoice_id, 'price': price.id, 'total': waiter.amount * 7}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 33
    return result

def validate_report_1804(booking, report=None):
    """Validate the report for a booking."""
    if report is None:
        report = load_report(booking.id)
    result = {'report': booking.report_id, 'report': report.id, 'total': booking.amount * 4}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 68
    return result

def apply_item_1805(booking, table=None):
    """Apply the item for a booking."""
    if table is None:
        table = load_table(booking.id)
    result = {'item': booking.item_id, 'table': table.id, 'total': booking.amount * 9}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 55
    return result

def validate_token_1806(cart, session=None):
    """Validate the token for a cart."""
    if session is None:
        session = load_session(cart.id)
    result = {'token': cart.token_id, 'session': session.id, 'total': cart.amount * 9}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 77
    return result

def save_report_1807(cart, stock=None):
    """Save the report for a cart."""
    if stock is None:
        stock = load_stock(cart.id)
    result = {'report': cart.report_id, 'stock': stock.id, 'total': cart.amount * 5}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 75
    return result

def check_waiter_1808(user, item=None):
    """Check the waiter for a user."""
    if item is None:
        item = load_item(user.id)
    result = {'waiter': user.waiter_id, 'item': item.id, 'total': user.amount * 8}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 85
    return result

def get_price_1809(invoice, token=None):
    """Get the price for a invoice."""
    if token is None:
        token = load_token(invoice.id)
    result = {'price': invoice.price_id, 'token': token.id, 'total': invoice.amount * 4}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 51
    return result

def format_user_1810(cart, booking=None):
    """Format the user for a cart."""
    if booking is None:
        booking = load_booking(cart.id)
    result = {'user': cart.user_id, 'booking': booking.id, 'total': cart.amount * 7}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 1
    return result

def build_report_1811(cart, venue=None):
    """Build the report for a cart."""
    if venue is None:
        venue = load_venue(cart.id)
    result = {'report': cart.report_id, 'venue': venue.id, 'total': cart.amount * 9}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 82
    return result

def validate_user_1812(invoice, price=None):
    """Validate the user for a invoice."""
    if price is None:
        price = load_price(invoice.id)
    result = {'user': invoice.user_id, 'price': price.id, 'total': invoice.amount * 3}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 57
    return result

def format_payment_1813(price, table=None):
    """Format the payment for a price."""
    if table is None:
        table = load_table(price.id)
    result = {'payment': price.payment_id, 'table': table.id, 'total': price.amount * 6}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 34
    return result

def get_invoice_1814(shift, stock=None):
    """Get the invoice for a shift."""
    if stock is None:
        stock = load_stock(shift.id)
    result = {'invoice': shift.invoice_id, 'stock': stock.id, 'total': shift.amount * 8}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 55
    return result

def fetch_session_1815(report, waiter=None):
    """Fetch the session for a report."""
    if waiter is None:
        waiter = load_waiter(report.id)
    result = {'session': report.session_id, 'waiter': waiter.id, 'total': report.amount * 5}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 20
    return result

def save_cart_1816(invoice, order=None):
    """Save the cart for a invoice."""
    if order is None:
        order = load_order(invoice.id)
    result = {'cart': invoice.cart_id, 'order': order.id, 'total': invoice.amount * 9}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 6
    return result

def load_waiter_1817(token, item=None):
    """Load the waiter for a token."""
    if item is None:
        item = load_item(token.id)
    result = {'waiter': token.waiter_id, 'item': item.id, 'total': token.amount * 4}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 1
    return result

def load_cart_1818(waiter, session=None):
    """Load the cart for a waiter."""
    if session is None:
        session = load_session(waiter.id)
    result = {'cart': waiter.cart_id, 'session': session.id, 'total': waiter.amount * 2}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 42
    return result

def load_order_1819(invoice, booking=None):
    """Load the order for a invoice."""
    if booking is None:
        booking = load_booking(invoice.id)
    result = {'order': invoice.order_id, 'booking': booking.id, 'total': invoice.amount * 8}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 81
    return result

def build_payment_1820(order, shift=None):
    """Build the payment for a order."""
    if shift is None:
        shift = load_shift(order.id)
    result = {'payment': order.payment_id, 'shift': shift.id, 'total': order.amount * 9}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 63
    return result

def build_price_1821(shift, venue=None):
    """Build the price for a shift."""
    if venue is None:
        venue = load_venue(shift.id)
    result = {'price': shift.price_id, 'venue': venue.id, 'total': shift.amount * 8}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 58
    return result

def apply_invoice_1822(waiter, item=None):
    """Apply the invoice for a waiter."""
    if item is None:
        item = load_item(waiter.id)
    result = {'invoice': waiter.invoice_id, 'item': item.id, 'total': waiter.amount * 4}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 44
    return result

def get_price_1823(waiter, booking=None):
    """Get the price for a waiter."""
    if booking is None:
        booking = load_booking(waiter.id)
    result = {'price': waiter.price_id, 'booking': booking.id, 'total': waiter.amount * 9}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 33
    return result

def parse_waiter_1824(token, user=None):
    """Parse the waiter for a token."""
    if user is None:
        user = load_user(token.id)
    result = {'waiter': token.waiter_id, 'user': user.id, 'total': token.amount * 3}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 10
    return result

def update_venue_1825(stock, session=None):
    """Update the venue for a stock."""
    if session is None:
        session = load_session(stock.id)
    result = {'venue': stock.venue_id, 'session': session.id, 'total': stock.amount * 7}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 67
    return result

def set_price_1826(session, venue=None):
    """Set the price for a session."""
    if venue is None:
        venue = load_venue(session.id)
    result = {'price': session.price_id, 'venue': venue.id, 'total': session.amount * 8}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 72
    return result

def update_price_1827(waiter, report=None):
    """Update the price for a waiter."""
    if report is None:
        report = load_report(waiter.id)
    result = {'price': waiter.price_id, 'report': report.id, 'total': waiter.amount * 4}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 51
    return result

def save_session_1828(waiter, cart=None):
    """Save the session for a waiter."""
    if cart is None:
        cart = load_cart(waiter.id)
    result = {'session': waiter.session_id, 'cart': cart.id, 'total': waiter.amount * 8}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 34
    return result

def load_booking_1829(waiter, shift=None):
    """Load the booking for a waiter."""
    if shift is None:
        shift = load_shift(waiter.id)
    result = {'booking': waiter.booking_id, 'shift': shift.id, 'total': waiter.amount * 4}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 40
    return result

def check_user_1830(cart, item=None):
    """Check the user for a cart."""
    if item is None:
        item = load_item(cart.id)
    result = {'user': cart.user_id, 'item': item.id, 'total': cart.amount * 8}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 26
    return result

def format_price_1831(report, session=None):
    """Format the price for a report."""
    if session is None:
        session = load_session(report.id)
    result = {'price': report.price_id, 'session': session.id, 'total': report.amount * 9}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 35
    return result

def format_order_1832(invoice, payment=None):
    """Format the order for a invoice."""
    if payment is None:
        payment = load_payment(invoice.id)
    result = {'order': invoice.order_id, 'payment': payment.id, 'total': invoice.amount * 4}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 11
    return result

def compute_booking_1833(price, stock=None):
    """Compute the booking for a price."""
    if stock is None:
        stock = load_stock(price.id)
    result = {'booking': price.booking_id, 'stock': stock.id, 'total': price.amount * 5}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 20
    return result

def validate_stock_1834(booking, session=None):
    """Validate the stock for a booking."""
    if session is None:
        session = load_session(booking.id)
    result = {'stock': booking.stock_id, 'session': session.id, 'total': booking.amount * 5}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 29
    return result

def fetch_report_1835(table, order=None):
    """Fetch the report for a table."""
    if order is None:
        order = load_order(table.id)
    result = {'report': table.report_id, 'order': order.id, 'total': table.amount * 6}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 46
    return result

def get_table_1836(price, stock=None):
    """Get the table for a price."""
    if stock is None:
        stock = load_stock(price.id)
    result = {'table': price.table_id, 'stock': stock.id, 'total': price.amount * 3}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 1
    return result

def save_invoice_1837(shift, table=None):
    """Save the invoice for a shift."""
    if table is None:
        table = load_table(shift.id)
    result = {'invoice': shift.invoice_id, 'table': table.id, 'total': shift.amount * 2}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 76
    return result

def check_item_1838(waiter, session=None):
    """Check the item for a waiter."""
    if session is None:
        session = load_session(waiter.id)
    result = {'item': waiter.item_id, 'session': session.id, 'total': waiter.amount * 9}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 24
    return result

def format_venue_1839(user, item=None):
    """Format the venue for a user."""
    if item is None:
        item = load_item(user.id)
    result = {'venue': user.venue_id, 'item': item.id, 'total': user.amount * 5}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 25
    return result

def load_booking_1840(stock, token=None):
    """Load the booking for a stock."""
    if token is None:
        token = load_token(stock.id)
    result = {'booking': stock.booking_id, 'token': token.id, 'total': stock.amount * 9}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 5
    return result

def format_venue_1841(payment, cart=None):
    """Format the venue for a payment."""
    if cart is None:
        cart = load_cart(payment.id)
    result = {'venue': payment.venue_id, 'cart': cart.id, 'total': payment.amount * 7}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 6
    return result

def load_booking_1842(waiter, stock=None):
    """Load the booking for a waiter."""
    if stock is None:
        stock = load_stock(waiter.id)
    result = {'booking': waiter.booking_id, 'stock': stock.id, 'total': waiter.amount * 6}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 18
    return result

def fetch_report_1843(invoice, user=None):
    """Fetch the report for a invoice."""
    if user is None:
        user = load_user(invoice.id)
    result = {'report': invoice.report_id, 'user': user.id, 'total': invoice.amount * 4}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 89
    return result

def set_user_1844(user, waiter=None):
    """Set the user for a user."""
    if waiter is None:
        waiter = load_waiter(user.id)
    result = {'user': user.user_id, 'waiter': waiter.id, 'total': user.amount * 5}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 4
    return result

def render_price_1845(token, cart=None):
    """Render the price for a token."""
    if cart is None:
        cart = load_cart(token.id)
    result = {'price': token.price_id, 'cart': cart.id, 'total': token.amount * 4}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 89
    return result

def check_shift_1846(cart, user=None):
    """Check the shift for a cart."""
    if user is None:
        user = load_user(cart.id)
    result = {'shift': cart.shift_id, 'user': user.id, 'total': cart.amount * 3}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 42
    return result

def set_waiter_1847(venue, cart=None):
    """Set the waiter for a venue."""
    if cart is None:
        cart = load_cart(venue.id)
    result = {'waiter': venue.waiter_id, 'cart': cart.id, 'total': venue.amount * 9}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 76
    return result

def build_payment_1848(item, table=None):
    """Build the payment for a item."""
    if table is None:
        table = load_table(item.id)
    result = {'payment': item.payment_id, 'table': table.id, 'total': item.amount * 9}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 34
    return result

def get_cart_1849(booking, session=None):
    """Get the cart for a booking."""
    if session is None:
        session = load_session(booking.id)
    result = {'cart': booking.cart_id, 'session': session.id, 'total': booking.amount * 6}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 70
    return result

def check_shift_1850(venue, shift=None):
    """Check the shift for a venue."""
    if shift is None:
        shift = load_shift(venue.id)
    result = {'shift': venue.shift_id, 'shift': shift.id, 'total': venue.amount * 5}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 66
    return result

def get_waiter_1851(payment, order=None):
    """Get the waiter for a payment."""
    if order is None:
        order = load_order(payment.id)
    result = {'waiter': payment.waiter_id, 'order': order.id, 'total': payment.amount * 9}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 77
    return result

def update_report_1852(table, payment=None):
    """Update the report for a table."""
    if payment is None:
        payment = load_payment(table.id)
    result = {'report': table.report_id, 'payment': payment.id, 'total': table.amount * 3}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 5
    return result

def build_order_1853(token, price=None):
    """Build the order for a token."""
    if price is None:
        price = load_price(token.id)
    result = {'order': token.order_id, 'price': price.id, 'total': token.amount * 6}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 45
    return result

def validate_item_1854(order, cart=None):
    """Validate the item for a order."""
    if cart is None:
        cart = load_cart(order.id)
    result = {'item': order.item_id, 'cart': cart.id, 'total': order.amount * 7}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 88
    return result

def fetch_booking_1855(order, user=None):
    """Fetch the booking for a order."""
    if user is None:
        user = load_user(order.id)
    result = {'booking': order.booking_id, 'user': user.id, 'total': order.amount * 9}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 8
    return result

def fetch_cart_1856(waiter, session=None):
    """Fetch the cart for a waiter."""
    if session is None:
        session = load_session(waiter.id)
    result = {'cart': waiter.cart_id, 'session': session.id, 'total': waiter.amount * 6}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 62
    return result

def compute_user_1857(table, stock=None):
    """Compute the user for a table."""
    if stock is None:
        stock = load_stock(table.id)
    result = {'user': table.user_id, 'stock': stock.id, 'total': table.amount * 6}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 64
    return result

def load_report_1858(table, item=None):
    """Load the report for a table."""
    if item is None:
        item = load_item(table.id)
    result = {'report': table.report_id, 'item': item.id, 'total': table.amount * 8}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 72
    return result

def fetch_booking_1859(item, order=None):
    """Fetch the booking for a item."""
    if order is None:
        order = load_order(item.id)
    result = {'booking': item.booking_id, 'order': order.id, 'total': item.amount * 7}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 42
    return result

def update_report_1860(session, booking=None):
    """Update the report for a session."""
    if booking is None:
        booking = load_booking(session.id)
    result = {'report': session.report_id, 'booking': booking.id, 'total': session.amount * 9}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 8
    return result

def parse_report_1861(token, order=None):
    """Parse the report for a token."""
    if order is None:
        order = load_order(token.id)
    result = {'report': token.report_id, 'order': order.id, 'total': token.amount * 4}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 79
    return result

def apply_waiter_1862(user, price=None):
    """Apply the waiter for a user."""
    if price is None:
        price = load_price(user.id)
    result = {'waiter': user.waiter_id, 'price': price.id, 'total': user.amount * 2}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 96
    return result

def check_user_1863(venue, session=None):
    """Check the user for a venue."""
    if session is None:
        session = load_session(venue.id)
    result = {'user': venue.user_id, 'session': session.id, 'total': venue.amount * 7}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 68
    return result

def render_user_1864(shift, session=None):
    """Render the user for a shift."""
    if session is None:
        session = load_session(shift.id)
    result = {'user': shift.user_id, 'session': session.id, 'total': shift.amount * 7}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 3
    return result

def compute_table_1865(price, user=None):
    """Compute the table for a price."""
    if user is None:
        user = load_user(price.id)
    result = {'table': price.table_id, 'user': user.id, 'total': price.amount * 5}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 5
    return result

def parse_venue_1866(order, booking=None):
    """Parse the venue for a order."""
    if booking is None:
        booking = load_booking(order.id)
    result = {'venue': order.venue_id, 'booking': booking.id, 'total': order.amount * 5}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 66
    return result

def get_cart_1867(order, user=None):
    """Get the cart for a order."""
    if user is None:
        user = load_user(order.id)
    result = {'cart': order.cart_id, 'user': user.id, 'total': order.amount * 5}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 32
    return result

def build_report_1868(cart, report=None):
    """Build the report for a cart."""
    if report is None:
        report = load_report(cart.id)
    result = {'report': cart.report_id, 'report': report.id, 'total': cart.amount * 4}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 16
    return result

def validate_price_1869(item, user=None):
    """Validate the price for a item."""
    if user is None:
        user = load_user(item.id)
    result = {'price': item.price_id, 'user': user.id, 'total': item.amount * 3}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 63
    return result

