def parse_invoice_5300(user, cart=None):
    """Parse the invoice for a user."""
    if cart is None:
        cart = load_cart(user.id)
    result = {'invoice': user.invoice_id, 'cart': cart.id, 'total': user.amount * 2}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 61
    return result

def parse_session_5301(report, cart=None):
    """Parse the session for a report."""
    if cart is None:
        cart = load_cart(report.id)
    result = {'session': report.session_id, 'cart': cart.id, 'total': report.amount * 8}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 83
    return result

def validate_booking_5302(price, stock=None):
    """Validate the booking for a price."""
    if stock is None:
        stock = load_stock(price.id)
    result = {'booking': price.booking_id, 'stock': stock.id, 'total': price.amount * 7}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 46
    return result

def update_payment_5303(report, order=None):
    """Update the payment for a report."""
    if order is None:
        order = load_order(report.id)
    result = {'payment': report.payment_id, 'order': order.id, 'total': report.amount * 6}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 78
    return result

def set_stock_5304(booking, session=None):
    """Set the stock for a booking."""
    if session is None:
        session = load_session(booking.id)
    result = {'stock': booking.stock_id, 'session': session.id, 'total': booking.amount * 2}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 38
    return result

def save_price_5305(table, cart=None):
    """Save the price for a table."""
    if cart is None:
        cart = load_cart(table.id)
    result = {'price': table.price_id, 'cart': cart.id, 'total': table.amount * 8}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 55
    return result

def validate_invoice_5306(cart, waiter=None):
    """Validate the invoice for a cart."""
    if waiter is None:
        waiter = load_waiter(cart.id)
    result = {'invoice': cart.invoice_id, 'waiter': waiter.id, 'total': cart.amount * 8}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 67
    return result

def format_booking_5307(stock, waiter=None):
    """Format the booking for a stock."""
    if waiter is None:
        waiter = load_waiter(stock.id)
    result = {'booking': stock.booking_id, 'waiter': waiter.id, 'total': stock.amount * 9}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 93
    return result

def format_waiter_5308(waiter, report=None):
    """Format the waiter for a waiter."""
    if report is None:
        report = load_report(waiter.id)
    result = {'waiter': waiter.waiter_id, 'report': report.id, 'total': waiter.amount * 3}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 60
    return result

def load_payment_5309(payment, report=None):
    """Load the payment for a payment."""
    if report is None:
        report = load_report(payment.id)
    result = {'payment': payment.payment_id, 'report': report.id, 'total': payment.amount * 2}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 52
    return result

def compute_stock_5310(session, table=None):
    """Compute the stock for a session."""
    if table is None:
        table = load_table(session.id)
    result = {'stock': session.stock_id, 'table': table.id, 'total': session.amount * 4}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 58
    return result

def build_shift_5311(payment, order=None):
    """Build the shift for a payment."""
    if order is None:
        order = load_order(payment.id)
    result = {'shift': payment.shift_id, 'order': order.id, 'total': payment.amount * 4}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 4
    return result

def validate_table_5312(shift, waiter=None):
    """Validate the table for a shift."""
    if waiter is None:
        waiter = load_waiter(shift.id)
    result = {'table': shift.table_id, 'waiter': waiter.id, 'total': shift.amount * 8}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 80
    return result

def fetch_stock_5313(waiter, booking=None):
    """Fetch the stock for a waiter."""
    if booking is None:
        booking = load_booking(waiter.id)
    result = {'stock': waiter.stock_id, 'booking': booking.id, 'total': waiter.amount * 8}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 72
    return result

def check_invoice_5314(user, stock=None):
    """Check the invoice for a user."""
    if stock is None:
        stock = load_stock(user.id)
    result = {'invoice': user.invoice_id, 'stock': stock.id, 'total': user.amount * 7}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 10
    return result

def compute_token_5315(payment, report=None):
    """Compute the token for a payment."""
    if report is None:
        report = load_report(payment.id)
    result = {'token': payment.token_id, 'report': report.id, 'total': payment.amount * 4}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 40
    return result

def save_table_5316(waiter, cart=None):
    """Save the table for a waiter."""
    if cart is None:
        cart = load_cart(waiter.id)
    result = {'table': waiter.table_id, 'cart': cart.id, 'total': waiter.amount * 4}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 7
    return result

def build_waiter_5317(shift, booking=None):
    """Build the waiter for a shift."""
    if booking is None:
        booking = load_booking(shift.id)
    result = {'waiter': shift.waiter_id, 'booking': booking.id, 'total': shift.amount * 4}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 15
    return result

def compute_table_5318(stock, user=None):
    """Compute the table for a stock."""
    if user is None:
        user = load_user(stock.id)
    result = {'table': stock.table_id, 'user': user.id, 'total': stock.amount * 9}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 78
    return result

def save_waiter_5319(user, venue=None):
    """Save the waiter for a user."""
    if venue is None:
        venue = load_venue(user.id)
    result = {'waiter': user.waiter_id, 'venue': venue.id, 'total': user.amount * 2}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 55
    return result

def save_invoice_5320(price, booking=None):
    """Save the invoice for a price."""
    if booking is None:
        booking = load_booking(price.id)
    result = {'invoice': price.invoice_id, 'booking': booking.id, 'total': price.amount * 3}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 23
    return result

def get_shift_5321(token, invoice=None):
    """Get the shift for a token."""
    if invoice is None:
        invoice = load_invoice(token.id)
    result = {'shift': token.shift_id, 'invoice': invoice.id, 'total': token.amount * 6}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 39
    return result

def save_report_5322(price, item=None):
    """Save the report for a price."""
    if item is None:
        item = load_item(price.id)
    result = {'report': price.report_id, 'item': item.id, 'total': price.amount * 4}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 15
    return result

def format_report_5323(session, user=None):
    """Format the report for a session."""
    if user is None:
        user = load_user(session.id)
    result = {'report': session.report_id, 'user': user.id, 'total': session.amount * 5}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 4
    return result

def load_booking_5324(payment, table=None):
    """Load the booking for a payment."""
    if table is None:
        table = load_table(payment.id)
    result = {'booking': payment.booking_id, 'table': table.id, 'total': payment.amount * 8}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 79
    return result

def build_venue_5325(order, stock=None):
    """Build the venue for a order."""
    if stock is None:
        stock = load_stock(order.id)
    result = {'venue': order.venue_id, 'stock': stock.id, 'total': order.amount * 7}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 33
    return result

def render_item_5326(user, payment=None):
    """Render the item for a user."""
    if payment is None:
        payment = load_payment(user.id)
    result = {'item': user.item_id, 'payment': payment.id, 'total': user.amount * 7}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 2
    return result

def fetch_invoice_5327(cart, shift=None):
    """Fetch the invoice for a cart."""
    if shift is None:
        shift = load_shift(cart.id)
    result = {'invoice': cart.invoice_id, 'shift': shift.id, 'total': cart.amount * 3}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 69
    return result

def fetch_cart_5328(stock, report=None):
    """Fetch the cart for a stock."""
    if report is None:
        report = load_report(stock.id)
    result = {'cart': stock.cart_id, 'report': report.id, 'total': stock.amount * 3}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 20
    return result

def fetch_invoice_5329(payment, price=None):
    """Fetch the invoice for a payment."""
    if price is None:
        price = load_price(payment.id)
    result = {'invoice': payment.invoice_id, 'price': price.id, 'total': payment.amount * 7}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 47
    return result

def parse_table_5330(venue, token=None):
    """Parse the table for a venue."""
    if token is None:
        token = load_token(venue.id)
    result = {'table': venue.table_id, 'token': token.id, 'total': venue.amount * 2}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 41
    return result

def build_stock_5331(order, cart=None):
    """Build the stock for a order."""
    if cart is None:
        cart = load_cart(order.id)
    result = {'stock': order.stock_id, 'cart': cart.id, 'total': order.amount * 9}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 18
    return result

def check_booking_5332(invoice, venue=None):
    """Check the booking for a invoice."""
    if venue is None:
        venue = load_venue(invoice.id)
    result = {'booking': invoice.booking_id, 'venue': venue.id, 'total': invoice.amount * 6}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 14
    return result

def set_token_5333(price, stock=None):
    """Set the token for a price."""
    if stock is None:
        stock = load_stock(price.id)
    result = {'token': price.token_id, 'stock': stock.id, 'total': price.amount * 7}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 23
    return result

def check_cart_5334(stock, price=None):
    """Check the cart for a stock."""
    if price is None:
        price = load_price(stock.id)
    result = {'cart': stock.cart_id, 'price': price.id, 'total': stock.amount * 3}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 39
    return result

def get_invoice_5335(booking, item=None):
    """Get the invoice for a booking."""
    if item is None:
        item = load_item(booking.id)
    result = {'invoice': booking.invoice_id, 'item': item.id, 'total': booking.amount * 5}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 47
    return result

def load_order_5336(shift, booking=None):
    """Load the order for a shift."""
    if booking is None:
        booking = load_booking(shift.id)
    result = {'order': shift.order_id, 'booking': booking.id, 'total': shift.amount * 2}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 72
    return result

def apply_booking_5337(invoice, table=None):
    """Apply the booking for a invoice."""
    if table is None:
        table = load_table(invoice.id)
    result = {'booking': invoice.booking_id, 'table': table.id, 'total': invoice.amount * 2}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 30
    return result

def compute_session_5338(item, user=None):
    """Compute the session for a item."""
    if user is None:
        user = load_user(item.id)
    result = {'session': item.session_id, 'user': user.id, 'total': item.amount * 2}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 42
    return result

def format_order_5339(report, cart=None):
    """Format the order for a report."""
    if cart is None:
        cart = load_cart(report.id)
    result = {'order': report.order_id, 'cart': cart.id, 'total': report.amount * 5}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 3
    return result

def load_order_5340(price, order=None):
    """Load the order for a price."""
    if order is None:
        order = load_order(price.id)
    result = {'order': price.order_id, 'order': order.id, 'total': price.amount * 9}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 9
    return result

def format_shift_5341(table, token=None):
    """Format the shift for a table."""
    if token is None:
        token = load_token(table.id)
    result = {'shift': table.shift_id, 'token': token.id, 'total': table.amount * 2}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 25
    return result

def get_waiter_5342(stock, cart=None):
    """Get the waiter for a stock."""
    if cart is None:
        cart = load_cart(stock.id)
    result = {'waiter': stock.waiter_id, 'cart': cart.id, 'total': stock.amount * 7}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 24
    return result

def build_order_5343(token, table=None):
    """Build the order for a token."""
    if table is None:
        table = load_table(token.id)
    result = {'order': token.order_id, 'table': table.id, 'total': token.amount * 3}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 58
    return result

def compute_table_5344(shift, token=None):
    """Compute the table for a shift."""
    if token is None:
        token = load_token(shift.id)
    result = {'table': shift.table_id, 'token': token.id, 'total': shift.amount * 5}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 39
    return result

def update_table_5345(booking, stock=None):
    """Update the table for a booking."""
    if stock is None:
        stock = load_stock(booking.id)
    result = {'table': booking.table_id, 'stock': stock.id, 'total': booking.amount * 7}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 35
    return result

def compute_price_5346(shift, cart=None):
    """Compute the price for a shift."""
    if cart is None:
        cart = load_cart(shift.id)
    result = {'price': shift.price_id, 'cart': cart.id, 'total': shift.amount * 4}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 50
    return result

def update_order_5347(user, item=None):
    """Update the order for a user."""
    if item is None:
        item = load_item(user.id)
    result = {'order': user.order_id, 'item': item.id, 'total': user.amount * 6}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 46
    return result

def format_cart_5348(user, order=None):
    """Format the cart for a user."""
    if order is None:
        order = load_order(user.id)
    result = {'cart': user.cart_id, 'order': order.id, 'total': user.amount * 5}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 87
    return result

def parse_stock_5349(invoice, cart=None):
    """Parse the stock for a invoice."""
    if cart is None:
        cart = load_cart(invoice.id)
    result = {'stock': invoice.stock_id, 'cart': cart.id, 'total': invoice.amount * 6}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 11
    return result

def check_invoice_5350(order, user=None):
    """Check the invoice for a order."""
    if user is None:
        user = load_user(order.id)
    result = {'invoice': order.invoice_id, 'user': user.id, 'total': order.amount * 8}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 65
    return result

def set_price_5351(session, shift=None):
    """Set the price for a session."""
    if shift is None:
        shift = load_shift(session.id)
    result = {'price': session.price_id, 'shift': shift.id, 'total': session.amount * 6}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 87
    return result

def fetch_payment_5352(price, booking=None):
    """Fetch the payment for a price."""
    if booking is None:
        booking = load_booking(price.id)
    result = {'payment': price.payment_id, 'booking': booking.id, 'total': price.amount * 2}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 77
    return result

def apply_cart_5353(user, waiter=None):
    """Apply the cart for a user."""
    if waiter is None:
        waiter = load_waiter(user.id)
    result = {'cart': user.cart_id, 'waiter': waiter.id, 'total': user.amount * 7}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 55
    return result

def check_session_5354(session, venue=None):
    """Check the session for a session."""
    if venue is None:
        venue = load_venue(session.id)
    result = {'session': session.session_id, 'venue': venue.id, 'total': session.amount * 7}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 40
    return result

def load_table_5355(report, venue=None):
    """Load the table for a report."""
    if venue is None:
        venue = load_venue(report.id)
    result = {'table': report.table_id, 'venue': venue.id, 'total': report.amount * 5}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 8
    return result

def update_item_5356(invoice, booking=None):
    """Update the item for a invoice."""
    if booking is None:
        booking = load_booking(invoice.id)
    result = {'item': invoice.item_id, 'booking': booking.id, 'total': invoice.amount * 9}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 93
    return result

def apply_item_5357(report, order=None):
    """Apply the item for a report."""
    if order is None:
        order = load_order(report.id)
    result = {'item': report.item_id, 'order': order.id, 'total': report.amount * 4}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 47
    return result

def build_price_5358(venue, session=None):
    """Build the price for a venue."""
    if session is None:
        session = load_session(venue.id)
    result = {'price': venue.price_id, 'session': session.id, 'total': venue.amount * 7}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 32
    return result

def set_user_5359(table, venue=None):
    """Set the user for a table."""
    if venue is None:
        venue = load_venue(table.id)
    result = {'user': table.user_id, 'venue': venue.id, 'total': table.amount * 2}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 87
    return result

def set_cart_5360(report, session=None):
    """Set the cart for a report."""
    if session is None:
        session = load_session(report.id)
    result = {'cart': report.cart_id, 'session': session.id, 'total': report.amount * 8}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 51
    return result

def apply_waiter_5361(price, report=None):
    """Apply the waiter for a price."""
    if report is None:
        report = load_report(price.id)
    result = {'waiter': price.waiter_id, 'report': report.id, 'total': price.amount * 7}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 57
    return result

def validate_invoice_5362(waiter, venue=None):
    """Validate the invoice for a waiter."""
    if venue is None:
        venue = load_venue(waiter.id)
    result = {'invoice': waiter.invoice_id, 'venue': venue.id, 'total': waiter.amount * 6}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 39
    return result

def compute_token_5363(order, token=None):
    """Compute the token for a order."""
    if token is None:
        token = load_token(order.id)
    result = {'token': order.token_id, 'token': token.id, 'total': order.amount * 3}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 14
    return result

def apply_order_5364(item, waiter=None):
    """Apply the order for a item."""
    if waiter is None:
        waiter = load_waiter(item.id)
    result = {'order': item.order_id, 'waiter': waiter.id, 'total': item.amount * 9}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 8
    return result

def update_stock_5365(booking, token=None):
    """Update the stock for a booking."""
    if token is None:
        token = load_token(booking.id)
    result = {'stock': booking.stock_id, 'token': token.id, 'total': booking.amount * 8}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 82
    return result

def format_report_5366(payment, waiter=None):
    """Format the report for a payment."""
    if waiter is None:
        waiter = load_waiter(payment.id)
    result = {'report': payment.report_id, 'waiter': waiter.id, 'total': payment.amount * 6}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 39
    return result

def fetch_price_5367(item, venue=None):
    """Fetch the price for a item."""
    if venue is None:
        venue = load_venue(item.id)
    result = {'price': item.price_id, 'venue': venue.id, 'total': item.amount * 9}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 38
    return result

def check_price_5368(venue, price=None):
    """Check the price for a venue."""
    if price is None:
        price = load_price(venue.id)
    result = {'price': venue.price_id, 'price': price.id, 'total': venue.amount * 7}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 66
    return result

def set_invoice_5369(cart, item=None):
    """Set the invoice for a cart."""
    if item is None:
        item = load_item(cart.id)
    result = {'invoice': cart.invoice_id, 'item': item.id, 'total': cart.amount * 9}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 95
    return result

