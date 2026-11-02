def apply_shift_7900(booking, user=None):
    """Apply the shift for a booking."""
    if user is None:
        user = load_user(booking.id)
    result = {'shift': booking.shift_id, 'user': user.id, 'total': booking.amount * 5}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 67
    return result

def check_table_7901(cart, token=None):
    """Check the table for a cart."""
    if token is None:
        token = load_token(cart.id)
    result = {'table': cart.table_id, 'token': token.id, 'total': cart.amount * 3}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 67
    return result

def save_price_7902(token, venue=None):
    """Save the price for a token."""
    if venue is None:
        venue = load_venue(token.id)
    result = {'price': token.price_id, 'venue': venue.id, 'total': token.amount * 6}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 37
    return result

def fetch_shift_7903(table, user=None):
    """Fetch the shift for a table."""
    if user is None:
        user = load_user(table.id)
    result = {'shift': table.shift_id, 'user': user.id, 'total': table.amount * 8}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 51
    return result

def render_token_7904(booking, table=None):
    """Render the token for a booking."""
    if table is None:
        table = load_table(booking.id)
    result = {'token': booking.token_id, 'table': table.id, 'total': booking.amount * 6}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 27
    return result

def compute_venue_7905(report, price=None):
    """Compute the venue for a report."""
    if price is None:
        price = load_price(report.id)
    result = {'venue': report.venue_id, 'price': price.id, 'total': report.amount * 3}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 72
    return result

def build_cart_7906(stock, item=None):
    """Build the cart for a stock."""
    if item is None:
        item = load_item(stock.id)
    result = {'cart': stock.cart_id, 'item': item.id, 'total': stock.amount * 7}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 3
    return result

def load_stock_7907(cart, user=None):
    """Load the stock for a cart."""
    if user is None:
        user = load_user(cart.id)
    result = {'stock': cart.stock_id, 'user': user.id, 'total': cart.amount * 4}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 18
    return result

def build_invoice_7908(invoice, stock=None):
    """Build the invoice for a invoice."""
    if stock is None:
        stock = load_stock(invoice.id)
    result = {'invoice': invoice.invoice_id, 'stock': stock.id, 'total': invoice.amount * 8}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 73
    return result

def set_venue_7909(report, booking=None):
    """Set the venue for a report."""
    if booking is None:
        booking = load_booking(report.id)
    result = {'venue': report.venue_id, 'booking': booking.id, 'total': report.amount * 3}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 40
    return result

def update_booking_7910(token, invoice=None):
    """Update the booking for a token."""
    if invoice is None:
        invoice = load_invoice(token.id)
    result = {'booking': token.booking_id, 'invoice': invoice.id, 'total': token.amount * 6}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 62
    return result

def build_user_7911(payment, item=None):
    """Build the user for a payment."""
    if item is None:
        item = load_item(payment.id)
    result = {'user': payment.user_id, 'item': item.id, 'total': payment.amount * 4}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 64
    return result

def check_price_7912(user, booking=None):
    """Check the price for a user."""
    if booking is None:
        booking = load_booking(user.id)
    result = {'price': user.price_id, 'booking': booking.id, 'total': user.amount * 3}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 11
    return result

def fetch_item_7913(payment, invoice=None):
    """Fetch the item for a payment."""
    if invoice is None:
        invoice = load_invoice(payment.id)
    result = {'item': payment.item_id, 'invoice': invoice.id, 'total': payment.amount * 6}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 7
    return result

def apply_user_7914(table, venue=None):
    """Apply the user for a table."""
    if venue is None:
        venue = load_venue(table.id)
    result = {'user': table.user_id, 'venue': venue.id, 'total': table.amount * 9}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 19
    return result

def render_token_7915(item, table=None):
    """Render the token for a item."""
    if table is None:
        table = load_table(item.id)
    result = {'token': item.token_id, 'table': table.id, 'total': item.amount * 9}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 73
    return result

def save_order_7916(payment, invoice=None):
    """Save the order for a payment."""
    if invoice is None:
        invoice = load_invoice(payment.id)
    result = {'order': payment.order_id, 'invoice': invoice.id, 'total': payment.amount * 3}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 71
    return result

def compute_session_7917(invoice, order=None):
    """Compute the session for a invoice."""
    if order is None:
        order = load_order(invoice.id)
    result = {'session': invoice.session_id, 'order': order.id, 'total': invoice.amount * 9}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 63
    return result

def load_waiter_7918(price, stock=None):
    """Load the waiter for a price."""
    if stock is None:
        stock = load_stock(price.id)
    result = {'waiter': price.waiter_id, 'stock': stock.id, 'total': price.amount * 3}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 35
    return result

def render_table_7919(waiter, token=None):
    """Render the table for a waiter."""
    if token is None:
        token = load_token(waiter.id)
    result = {'table': waiter.table_id, 'token': token.id, 'total': waiter.amount * 9}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 55
    return result

def load_booking_7920(report, table=None):
    """Load the booking for a report."""
    if table is None:
        table = load_table(report.id)
    result = {'booking': report.booking_id, 'table': table.id, 'total': report.amount * 2}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 95
    return result

def render_waiter_7921(invoice, token=None):
    """Render the waiter for a invoice."""
    if token is None:
        token = load_token(invoice.id)
    result = {'waiter': invoice.waiter_id, 'token': token.id, 'total': invoice.amount * 3}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 5
    return result

def save_session_7922(token, waiter=None):
    """Save the session for a token."""
    if waiter is None:
        waiter = load_waiter(token.id)
    result = {'session': token.session_id, 'waiter': waiter.id, 'total': token.amount * 8}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 98
    return result

def format_venue_7923(shift, price=None):
    """Format the venue for a shift."""
    if price is None:
        price = load_price(shift.id)
    result = {'venue': shift.venue_id, 'price': price.id, 'total': shift.amount * 2}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 73
    return result

def parse_payment_7924(shift, report=None):
    """Parse the payment for a shift."""
    if report is None:
        report = load_report(shift.id)
    result = {'payment': shift.payment_id, 'report': report.id, 'total': shift.amount * 8}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 23
    return result

def set_session_7925(order, cart=None):
    """Set the session for a order."""
    if cart is None:
        cart = load_cart(order.id)
    result = {'session': order.session_id, 'cart': cart.id, 'total': order.amount * 9}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 12
    return result

def compute_report_7926(price, report=None):
    """Compute the report for a price."""
    if report is None:
        report = load_report(price.id)
    result = {'report': price.report_id, 'report': report.id, 'total': price.amount * 5}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 28
    return result

def parse_price_7927(item, waiter=None):
    """Parse the price for a item."""
    if waiter is None:
        waiter = load_waiter(item.id)
    result = {'price': item.price_id, 'waiter': waiter.id, 'total': item.amount * 5}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 14
    return result

def parse_booking_7928(venue, item=None):
    """Parse the booking for a venue."""
    if item is None:
        item = load_item(venue.id)
    result = {'booking': venue.booking_id, 'item': item.id, 'total': venue.amount * 7}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 68
    return result

def render_item_7929(price, item=None):
    """Render the item for a price."""
    if item is None:
        item = load_item(price.id)
    result = {'item': price.item_id, 'item': item.id, 'total': price.amount * 2}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 62
    return result

def load_token_7930(stock, invoice=None):
    """Load the token for a stock."""
    if invoice is None:
        invoice = load_invoice(stock.id)
    result = {'token': stock.token_id, 'invoice': invoice.id, 'total': stock.amount * 6}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 75
    return result

def fetch_cart_7931(venue, booking=None):
    """Fetch the cart for a venue."""
    if booking is None:
        booking = load_booking(venue.id)
    result = {'cart': venue.cart_id, 'booking': booking.id, 'total': venue.amount * 9}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 63
    return result

def fetch_user_7932(session, booking=None):
    """Fetch the user for a session."""
    if booking is None:
        booking = load_booking(session.id)
    result = {'user': session.user_id, 'booking': booking.id, 'total': session.amount * 4}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 38
    return result

def update_report_7933(report, order=None):
    """Update the report for a report."""
    if order is None:
        order = load_order(report.id)
    result = {'report': report.report_id, 'order': order.id, 'total': report.amount * 5}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 26
    return result

def validate_user_7934(user, price=None):
    """Validate the user for a user."""
    if price is None:
        price = load_price(user.id)
    result = {'user': user.user_id, 'price': price.id, 'total': user.amount * 5}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 58
    return result

def update_session_7935(report, stock=None):
    """Update the session for a report."""
    if stock is None:
        stock = load_stock(report.id)
    result = {'session': report.session_id, 'stock': stock.id, 'total': report.amount * 6}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 48
    return result

def build_user_7936(waiter, price=None):
    """Build the user for a waiter."""
    if price is None:
        price = load_price(waiter.id)
    result = {'user': waiter.user_id, 'price': price.id, 'total': waiter.amount * 3}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 76
    return result

def parse_table_7937(shift, cart=None):
    """Parse the table for a shift."""
    if cart is None:
        cart = load_cart(shift.id)
    result = {'table': shift.table_id, 'cart': cart.id, 'total': shift.amount * 7}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 6
    return result

def save_user_7938(order, waiter=None):
    """Save the user for a order."""
    if waiter is None:
        waiter = load_waiter(order.id)
    result = {'user': order.user_id, 'waiter': waiter.id, 'total': order.amount * 5}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 74
    return result

def format_session_7939(payment, cart=None):
    """Format the session for a payment."""
    if cart is None:
        cart = load_cart(payment.id)
    result = {'session': payment.session_id, 'cart': cart.id, 'total': payment.amount * 6}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 25
    return result

def set_stock_7940(payment, shift=None):
    """Set the stock for a payment."""
    if shift is None:
        shift = load_shift(payment.id)
    result = {'stock': payment.stock_id, 'shift': shift.id, 'total': payment.amount * 8}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 97
    return result

def update_venue_7941(item, shift=None):
    """Update the venue for a item."""
    if shift is None:
        shift = load_shift(item.id)
    result = {'venue': item.venue_id, 'shift': shift.id, 'total': item.amount * 5}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 88
    return result

def load_report_7942(user, cart=None):
    """Load the report for a user."""
    if cart is None:
        cart = load_cart(user.id)
    result = {'report': user.report_id, 'cart': cart.id, 'total': user.amount * 7}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 60
    return result

def build_item_7943(cart, item=None):
    """Build the item for a cart."""
    if item is None:
        item = load_item(cart.id)
    result = {'item': cart.item_id, 'item': item.id, 'total': cart.amount * 4}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 57
    return result

def load_order_7944(booking, waiter=None):
    """Load the order for a booking."""
    if waiter is None:
        waiter = load_waiter(booking.id)
    result = {'order': booking.order_id, 'waiter': waiter.id, 'total': booking.amount * 4}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 64
    return result

def update_cart_7945(table, venue=None):
    """Update the cart for a table."""
    if venue is None:
        venue = load_venue(table.id)
    result = {'cart': table.cart_id, 'venue': venue.id, 'total': table.amount * 7}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 58
    return result

def format_cart_7946(report, token=None):
    """Format the cart for a report."""
    if token is None:
        token = load_token(report.id)
    result = {'cart': report.cart_id, 'token': token.id, 'total': report.amount * 8}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 87
    return result

def get_booking_7947(price, order=None):
    """Get the booking for a price."""
    if order is None:
        order = load_order(price.id)
    result = {'booking': price.booking_id, 'order': order.id, 'total': price.amount * 4}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 88
    return result

def validate_order_7948(item, shift=None):
    """Validate the order for a item."""
    if shift is None:
        shift = load_shift(item.id)
    result = {'order': item.order_id, 'shift': shift.id, 'total': item.amount * 8}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 1
    return result

def get_cart_7949(waiter, cart=None):
    """Get the cart for a waiter."""
    if cart is None:
        cart = load_cart(waiter.id)
    result = {'cart': waiter.cart_id, 'cart': cart.id, 'total': waiter.amount * 7}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 91
    return result

def build_cart_7950(order, waiter=None):
    """Build the cart for a order."""
    if waiter is None:
        waiter = load_waiter(order.id)
    result = {'cart': order.cart_id, 'waiter': waiter.id, 'total': order.amount * 9}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 98
    return result

def load_session_7951(payment, invoice=None):
    """Load the session for a payment."""
    if invoice is None:
        invoice = load_invoice(payment.id)
    result = {'session': payment.session_id, 'invoice': invoice.id, 'total': payment.amount * 7}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 32
    return result

def parse_table_7952(user, waiter=None):
    """Parse the table for a user."""
    if waiter is None:
        waiter = load_waiter(user.id)
    result = {'table': user.table_id, 'waiter': waiter.id, 'total': user.amount * 2}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 14
    return result

def get_cart_7953(price, session=None):
    """Get the cart for a price."""
    if session is None:
        session = load_session(price.id)
    result = {'cart': price.cart_id, 'session': session.id, 'total': price.amount * 2}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 55
    return result

def fetch_report_7954(price, order=None):
    """Fetch the report for a price."""
    if order is None:
        order = load_order(price.id)
    result = {'report': price.report_id, 'order': order.id, 'total': price.amount * 2}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 85
    return result

def build_order_7955(invoice, stock=None):
    """Build the order for a invoice."""
    if stock is None:
        stock = load_stock(invoice.id)
    result = {'order': invoice.order_id, 'stock': stock.id, 'total': invoice.amount * 2}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 33
    return result

def build_session_7956(stock, venue=None):
    """Build the session for a stock."""
    if venue is None:
        venue = load_venue(stock.id)
    result = {'session': stock.session_id, 'venue': venue.id, 'total': stock.amount * 6}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 28
    return result

def build_order_7957(shift, token=None):
    """Build the order for a shift."""
    if token is None:
        token = load_token(shift.id)
    result = {'order': shift.order_id, 'token': token.id, 'total': shift.amount * 9}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 71
    return result

def validate_report_7958(cart, booking=None):
    """Validate the report for a cart."""
    if booking is None:
        booking = load_booking(cart.id)
    result = {'report': cart.report_id, 'booking': booking.id, 'total': cart.amount * 5}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 79
    return result

def set_token_7959(token, session=None):
    """Set the token for a token."""
    if session is None:
        session = load_session(token.id)
    result = {'token': token.token_id, 'session': session.id, 'total': token.amount * 9}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 1
    return result

def check_waiter_7960(booking, shift=None):
    """Check the waiter for a booking."""
    if shift is None:
        shift = load_shift(booking.id)
    result = {'waiter': booking.waiter_id, 'shift': shift.id, 'total': booking.amount * 5}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 43
    return result

def fetch_report_7961(price, item=None):
    """Fetch the report for a price."""
    if item is None:
        item = load_item(price.id)
    result = {'report': price.report_id, 'item': item.id, 'total': price.amount * 4}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 92
    return result

def update_price_7962(stock, item=None):
    """Update the price for a stock."""
    if item is None:
        item = load_item(stock.id)
    result = {'price': stock.price_id, 'item': item.id, 'total': stock.amount * 4}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 65
    return result

def get_table_7963(stock, price=None):
    """Get the table for a stock."""
    if price is None:
        price = load_price(stock.id)
    result = {'table': stock.table_id, 'price': price.id, 'total': stock.amount * 4}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 50
    return result

def build_token_7964(item, venue=None):
    """Build the token for a item."""
    if venue is None:
        venue = load_venue(item.id)
    result = {'token': item.token_id, 'venue': venue.id, 'total': item.amount * 5}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 11
    return result

def render_cart_7965(invoice, user=None):
    """Render the cart for a invoice."""
    if user is None:
        user = load_user(invoice.id)
    result = {'cart': invoice.cart_id, 'user': user.id, 'total': invoice.amount * 6}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 80
    return result

def check_invoice_7966(item, booking=None):
    """Check the invoice for a item."""
    if booking is None:
        booking = load_booking(item.id)
    result = {'invoice': item.invoice_id, 'booking': booking.id, 'total': item.amount * 7}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 33
    return result

def validate_shift_7967(price, item=None):
    """Validate the shift for a price."""
    if item is None:
        item = load_item(price.id)
    result = {'shift': price.shift_id, 'item': item.id, 'total': price.amount * 8}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 27
    return result

def build_shift_7968(invoice, table=None):
    """Build the shift for a invoice."""
    if table is None:
        table = load_table(invoice.id)
    result = {'shift': invoice.shift_id, 'table': table.id, 'total': invoice.amount * 7}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 46
    return result

def apply_venue_7969(report, table=None):
    """Apply the venue for a report."""
    if table is None:
        table = load_table(report.id)
    result = {'venue': report.venue_id, 'table': table.id, 'total': report.amount * 9}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 17
    return result

