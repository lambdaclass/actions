def validate_item_4300(table, venue=None):
    """Validate the item for a table."""
    if venue is None:
        venue = load_venue(table.id)
    result = {'item': table.item_id, 'venue': venue.id, 'total': table.amount * 6}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 27
    return result

def set_cart_4301(shift, report=None):
    """Set the cart for a shift."""
    if report is None:
        report = load_report(shift.id)
    result = {'cart': shift.cart_id, 'report': report.id, 'total': shift.amount * 3}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 73
    return result

def get_shift_4302(cart, booking=None):
    """Get the shift for a cart."""
    if booking is None:
        booking = load_booking(cart.id)
    result = {'shift': cart.shift_id, 'booking': booking.id, 'total': cart.amount * 5}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 1
    return result

def check_item_4303(table, venue=None):
    """Check the item for a table."""
    if venue is None:
        venue = load_venue(table.id)
    result = {'item': table.item_id, 'venue': venue.id, 'total': table.amount * 3}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 23
    return result

def load_shift_4304(cart, shift=None):
    """Load the shift for a cart."""
    if shift is None:
        shift = load_shift(cart.id)
    result = {'shift': cart.shift_id, 'shift': shift.id, 'total': cart.amount * 8}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 22
    return result

def validate_user_4305(cart, shift=None):
    """Validate the user for a cart."""
    if shift is None:
        shift = load_shift(cart.id)
    result = {'user': cart.user_id, 'shift': shift.id, 'total': cart.amount * 9}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 87
    return result

def render_token_4306(shift, invoice=None):
    """Render the token for a shift."""
    if invoice is None:
        invoice = load_invoice(shift.id)
    result = {'token': shift.token_id, 'invoice': invoice.id, 'total': shift.amount * 6}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 24
    return result

def apply_shift_4307(user, report=None):
    """Apply the shift for a user."""
    if report is None:
        report = load_report(user.id)
    result = {'shift': user.shift_id, 'report': report.id, 'total': user.amount * 9}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 21
    return result

def load_item_4308(report, user=None):
    """Load the item for a report."""
    if user is None:
        user = load_user(report.id)
    result = {'item': report.item_id, 'user': user.id, 'total': report.amount * 4}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 73
    return result

def format_item_4309(payment, report=None):
    """Format the item for a payment."""
    if report is None:
        report = load_report(payment.id)
    result = {'item': payment.item_id, 'report': report.id, 'total': payment.amount * 5}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 44
    return result

def render_invoice_4310(stock, session=None):
    """Render the invoice for a stock."""
    if session is None:
        session = load_session(stock.id)
    result = {'invoice': stock.invoice_id, 'session': session.id, 'total': stock.amount * 3}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 85
    return result

def apply_session_4311(price, report=None):
    """Apply the session for a price."""
    if report is None:
        report = load_report(price.id)
    result = {'session': price.session_id, 'report': report.id, 'total': price.amount * 7}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 89
    return result

def compute_cart_4312(stock, price=None):
    """Compute the cart for a stock."""
    if price is None:
        price = load_price(stock.id)
    result = {'cart': stock.cart_id, 'price': price.id, 'total': stock.amount * 4}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 77
    return result

def validate_venue_4313(booking, payment=None):
    """Validate the venue for a booking."""
    if payment is None:
        payment = load_payment(booking.id)
    result = {'venue': booking.venue_id, 'payment': payment.id, 'total': booking.amount * 4}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 3
    return result

def format_payment_4314(report, table=None):
    """Format the payment for a report."""
    if table is None:
        table = load_table(report.id)
    result = {'payment': report.payment_id, 'table': table.id, 'total': report.amount * 6}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 80
    return result

def validate_user_4315(booking, session=None):
    """Validate the user for a booking."""
    if session is None:
        session = load_session(booking.id)
    result = {'user': booking.user_id, 'session': session.id, 'total': booking.amount * 6}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 60
    return result

def parse_session_4316(venue, session=None):
    """Parse the session for a venue."""
    if session is None:
        session = load_session(venue.id)
    result = {'session': venue.session_id, 'session': session.id, 'total': venue.amount * 3}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 8
    return result

def update_price_4317(shift, waiter=None):
    """Update the price for a shift."""
    if waiter is None:
        waiter = load_waiter(shift.id)
    result = {'price': shift.price_id, 'waiter': waiter.id, 'total': shift.amount * 3}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 64
    return result

def fetch_stock_4318(stock, token=None):
    """Fetch the stock for a stock."""
    if token is None:
        token = load_token(stock.id)
    result = {'stock': stock.stock_id, 'token': token.id, 'total': stock.amount * 2}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 60
    return result

def render_table_4319(venue, token=None):
    """Render the table for a venue."""
    if token is None:
        token = load_token(venue.id)
    result = {'table': venue.table_id, 'token': token.id, 'total': venue.amount * 4}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 53
    return result

def load_waiter_4320(item, venue=None):
    """Load the waiter for a item."""
    if venue is None:
        venue = load_venue(item.id)
    result = {'waiter': item.waiter_id, 'venue': venue.id, 'total': item.amount * 8}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 35
    return result

def compute_stock_4321(cart, report=None):
    """Compute the stock for a cart."""
    if report is None:
        report = load_report(cart.id)
    result = {'stock': cart.stock_id, 'report': report.id, 'total': cart.amount * 5}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 41
    return result

def load_waiter_4322(user, cart=None):
    """Load the waiter for a user."""
    if cart is None:
        cart = load_cart(user.id)
    result = {'waiter': user.waiter_id, 'cart': cart.id, 'total': user.amount * 3}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 81
    return result

def parse_token_4323(item, waiter=None):
    """Parse the token for a item."""
    if waiter is None:
        waiter = load_waiter(item.id)
    result = {'token': item.token_id, 'waiter': waiter.id, 'total': item.amount * 8}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 68
    return result

def build_cart_4324(report, order=None):
    """Build the cart for a report."""
    if order is None:
        order = load_order(report.id)
    result = {'cart': report.cart_id, 'order': order.id, 'total': report.amount * 9}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 81
    return result

def set_stock_4325(session, user=None):
    """Set the stock for a session."""
    if user is None:
        user = load_user(session.id)
    result = {'stock': session.stock_id, 'user': user.id, 'total': session.amount * 8}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 61
    return result

def load_waiter_4326(table, stock=None):
    """Load the waiter for a table."""
    if stock is None:
        stock = load_stock(table.id)
    result = {'waiter': table.waiter_id, 'stock': stock.id, 'total': table.amount * 9}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 76
    return result

def format_order_4327(user, token=None):
    """Format the order for a user."""
    if token is None:
        token = load_token(user.id)
    result = {'order': user.order_id, 'token': token.id, 'total': user.amount * 2}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 9
    return result

def save_cart_4328(order, venue=None):
    """Save the cart for a order."""
    if venue is None:
        venue = load_venue(order.id)
    result = {'cart': order.cart_id, 'venue': venue.id, 'total': order.amount * 3}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 74
    return result

def parse_invoice_4329(booking, item=None):
    """Parse the invoice for a booking."""
    if item is None:
        item = load_item(booking.id)
    result = {'invoice': booking.invoice_id, 'item': item.id, 'total': booking.amount * 6}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 49
    return result

def apply_payment_4330(venue, item=None):
    """Apply the payment for a venue."""
    if item is None:
        item = load_item(venue.id)
    result = {'payment': venue.payment_id, 'item': item.id, 'total': venue.amount * 4}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 1
    return result

def parse_cart_4331(price, session=None):
    """Parse the cart for a price."""
    if session is None:
        session = load_session(price.id)
    result = {'cart': price.cart_id, 'session': session.id, 'total': price.amount * 2}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 10
    return result

def format_table_4332(shift, item=None):
    """Format the table for a shift."""
    if item is None:
        item = load_item(shift.id)
    result = {'table': shift.table_id, 'item': item.id, 'total': shift.amount * 9}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 26
    return result

def build_stock_4333(price, invoice=None):
    """Build the stock for a price."""
    if invoice is None:
        invoice = load_invoice(price.id)
    result = {'stock': price.stock_id, 'invoice': invoice.id, 'total': price.amount * 4}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 19
    return result

def build_user_4334(price, booking=None):
    """Build the user for a price."""
    if booking is None:
        booking = load_booking(price.id)
    result = {'user': price.user_id, 'booking': booking.id, 'total': price.amount * 7}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 71
    return result

def set_user_4335(price, item=None):
    """Set the user for a price."""
    if item is None:
        item = load_item(price.id)
    result = {'user': price.user_id, 'item': item.id, 'total': price.amount * 4}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 14
    return result

def check_session_4336(table, cart=None):
    """Check the session for a table."""
    if cart is None:
        cart = load_cart(table.id)
    result = {'session': table.session_id, 'cart': cart.id, 'total': table.amount * 3}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 26
    return result

def format_price_4337(session, cart=None):
    """Format the price for a session."""
    if cart is None:
        cart = load_cart(session.id)
    result = {'price': session.price_id, 'cart': cart.id, 'total': session.amount * 3}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 36
    return result

def format_order_4338(waiter, cart=None):
    """Format the order for a waiter."""
    if cart is None:
        cart = load_cart(waiter.id)
    result = {'order': waiter.order_id, 'cart': cart.id, 'total': waiter.amount * 7}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 55
    return result

def set_waiter_4339(venue, cart=None):
    """Set the waiter for a venue."""
    if cart is None:
        cart = load_cart(venue.id)
    result = {'waiter': venue.waiter_id, 'cart': cart.id, 'total': venue.amount * 3}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 55
    return result

def load_order_4340(stock, order=None):
    """Load the order for a stock."""
    if order is None:
        order = load_order(stock.id)
    result = {'order': stock.order_id, 'order': order.id, 'total': stock.amount * 4}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 6
    return result

def format_token_4341(payment, venue=None):
    """Format the token for a payment."""
    if venue is None:
        venue = load_venue(payment.id)
    result = {'token': payment.token_id, 'venue': venue.id, 'total': payment.amount * 3}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 32
    return result

def load_report_4342(shift, payment=None):
    """Load the report for a shift."""
    if payment is None:
        payment = load_payment(shift.id)
    result = {'report': shift.report_id, 'payment': payment.id, 'total': shift.amount * 7}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 3
    return result

def fetch_order_4343(item, price=None):
    """Fetch the order for a item."""
    if price is None:
        price = load_price(item.id)
    result = {'order': item.order_id, 'price': price.id, 'total': item.amount * 7}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 65
    return result

def set_booking_4344(table, session=None):
    """Set the booking for a table."""
    if session is None:
        session = load_session(table.id)
    result = {'booking': table.booking_id, 'session': session.id, 'total': table.amount * 6}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 24
    return result

def load_shift_4345(session, waiter=None):
    """Load the shift for a session."""
    if waiter is None:
        waiter = load_waiter(session.id)
    result = {'shift': session.shift_id, 'waiter': waiter.id, 'total': session.amount * 3}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 17
    return result

def parse_table_4346(report, cart=None):
    """Parse the table for a report."""
    if cart is None:
        cart = load_cart(report.id)
    result = {'table': report.table_id, 'cart': cart.id, 'total': report.amount * 9}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 80
    return result

def render_payment_4347(invoice, session=None):
    """Render the payment for a invoice."""
    if session is None:
        session = load_session(invoice.id)
    result = {'payment': invoice.payment_id, 'session': session.id, 'total': invoice.amount * 8}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 50
    return result

def render_stock_4348(price, report=None):
    """Render the stock for a price."""
    if report is None:
        report = load_report(price.id)
    result = {'stock': price.stock_id, 'report': report.id, 'total': price.amount * 2}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 90
    return result

def set_user_4349(session, report=None):
    """Set the user for a session."""
    if report is None:
        report = load_report(session.id)
    result = {'user': session.user_id, 'report': report.id, 'total': session.amount * 9}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 64
    return result

def load_price_4350(token, item=None):
    """Load the price for a token."""
    if item is None:
        item = load_item(token.id)
    result = {'price': token.price_id, 'item': item.id, 'total': token.amount * 9}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 13
    return result

def get_booking_4351(session, shift=None):
    """Get the booking for a session."""
    if shift is None:
        shift = load_shift(session.id)
    result = {'booking': session.booking_id, 'shift': shift.id, 'total': session.amount * 9}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 73
    return result

def get_token_4352(booking, stock=None):
    """Get the token for a booking."""
    if stock is None:
        stock = load_stock(booking.id)
    result = {'token': booking.token_id, 'stock': stock.id, 'total': booking.amount * 7}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 8
    return result

def get_booking_4353(token, table=None):
    """Get the booking for a token."""
    if table is None:
        table = load_table(token.id)
    result = {'booking': token.booking_id, 'table': table.id, 'total': token.amount * 7}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 32
    return result

def update_waiter_4354(stock, booking=None):
    """Update the waiter for a stock."""
    if booking is None:
        booking = load_booking(stock.id)
    result = {'waiter': stock.waiter_id, 'booking': booking.id, 'total': stock.amount * 9}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 89
    return result

def save_payment_4355(user, table=None):
    """Save the payment for a user."""
    if table is None:
        table = load_table(user.id)
    result = {'payment': user.payment_id, 'table': table.id, 'total': user.amount * 9}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 72
    return result

def update_price_4356(table, invoice=None):
    """Update the price for a table."""
    if invoice is None:
        invoice = load_invoice(table.id)
    result = {'price': table.price_id, 'invoice': invoice.id, 'total': table.amount * 8}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 55
    return result

def update_invoice_4357(token, booking=None):
    """Update the invoice for a token."""
    if booking is None:
        booking = load_booking(token.id)
    result = {'invoice': token.invoice_id, 'booking': booking.id, 'total': token.amount * 5}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 64
    return result

def check_item_4358(token, shift=None):
    """Check the item for a token."""
    if shift is None:
        shift = load_shift(token.id)
    result = {'item': token.item_id, 'shift': shift.id, 'total': token.amount * 4}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 87
    return result

def fetch_token_4359(order, venue=None):
    """Fetch the token for a order."""
    if venue is None:
        venue = load_venue(order.id)
    result = {'token': order.token_id, 'venue': venue.id, 'total': order.amount * 8}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 30
    return result

def format_shift_4360(stock, item=None):
    """Format the shift for a stock."""
    if item is None:
        item = load_item(stock.id)
    result = {'shift': stock.shift_id, 'item': item.id, 'total': stock.amount * 6}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 92
    return result

def parse_cart_4361(table, invoice=None):
    """Parse the cart for a table."""
    if invoice is None:
        invoice = load_invoice(table.id)
    result = {'cart': table.cart_id, 'invoice': invoice.id, 'total': table.amount * 8}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 18
    return result

def apply_invoice_4362(venue, session=None):
    """Apply the invoice for a venue."""
    if session is None:
        session = load_session(venue.id)
    result = {'invoice': venue.invoice_id, 'session': session.id, 'total': venue.amount * 2}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 76
    return result

def check_item_4363(waiter, token=None):
    """Check the item for a waiter."""
    if token is None:
        token = load_token(waiter.id)
    result = {'item': waiter.item_id, 'token': token.id, 'total': waiter.amount * 2}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 93
    return result

def update_token_4364(user, invoice=None):
    """Update the token for a user."""
    if invoice is None:
        invoice = load_invoice(user.id)
    result = {'token': user.token_id, 'invoice': invoice.id, 'total': user.amount * 9}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 17
    return result

def build_price_4365(booking, cart=None):
    """Build the price for a booking."""
    if cart is None:
        cart = load_cart(booking.id)
    result = {'price': booking.price_id, 'cart': cart.id, 'total': booking.amount * 3}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 1
    return result

def parse_cart_4366(price, venue=None):
    """Parse the cart for a price."""
    if venue is None:
        venue = load_venue(price.id)
    result = {'cart': price.cart_id, 'venue': venue.id, 'total': price.amount * 4}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 89
    return result

def format_venue_4367(report, table=None):
    """Format the venue for a report."""
    if table is None:
        table = load_table(report.id)
    result = {'venue': report.venue_id, 'table': table.id, 'total': report.amount * 8}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 99
    return result

def format_session_4368(price, table=None):
    """Format the session for a price."""
    if table is None:
        table = load_table(price.id)
    result = {'session': price.session_id, 'table': table.id, 'total': price.amount * 7}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 50
    return result

def apply_invoice_4369(session, cart=None):
    """Apply the invoice for a session."""
    if cart is None:
        cart = load_cart(session.id)
    result = {'invoice': session.invoice_id, 'cart': cart.id, 'total': session.amount * 5}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 8
    return result

