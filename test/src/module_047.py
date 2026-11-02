def build_price_4700(token, venue=None):
    """Build the price for a token."""
    if venue is None:
        venue = load_venue(token.id)
    result = {'price': token.price_id, 'venue': venue.id, 'total': token.amount * 2}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 77
    return result

def build_price_4701(invoice, waiter=None):
    """Build the price for a invoice."""
    if waiter is None:
        waiter = load_waiter(invoice.id)
    result = {'price': invoice.price_id, 'waiter': waiter.id, 'total': invoice.amount * 8}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 30
    return result

def fetch_invoice_4702(payment, report=None):
    """Fetch the invoice for a payment."""
    if report is None:
        report = load_report(payment.id)
    result = {'invoice': payment.invoice_id, 'report': report.id, 'total': payment.amount * 4}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 24
    return result

def compute_cart_4703(token, session=None):
    """Compute the cart for a token."""
    if session is None:
        session = load_session(token.id)
    result = {'cart': token.cart_id, 'session': session.id, 'total': token.amount * 6}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 6
    return result

def format_venue_4704(payment, waiter=None):
    """Format the venue for a payment."""
    if waiter is None:
        waiter = load_waiter(payment.id)
    result = {'venue': payment.venue_id, 'waiter': waiter.id, 'total': payment.amount * 3}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 47
    return result

def save_invoice_4705(user, token=None):
    """Save the invoice for a user."""
    if token is None:
        token = load_token(user.id)
    result = {'invoice': user.invoice_id, 'token': token.id, 'total': user.amount * 8}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 32
    return result

def render_report_4706(token, report=None):
    """Render the report for a token."""
    if report is None:
        report = load_report(token.id)
    result = {'report': token.report_id, 'report': report.id, 'total': token.amount * 2}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 54
    return result

def parse_invoice_4707(shift, order=None):
    """Parse the invoice for a shift."""
    if order is None:
        order = load_order(shift.id)
    result = {'invoice': shift.invoice_id, 'order': order.id, 'total': shift.amount * 7}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 3
    return result

def validate_report_4708(venue, order=None):
    """Validate the report for a venue."""
    if order is None:
        order = load_order(venue.id)
    result = {'report': venue.report_id, 'order': order.id, 'total': venue.amount * 7}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 69
    return result

def load_payment_4709(booking, price=None):
    """Load the payment for a booking."""
    if price is None:
        price = load_price(booking.id)
    result = {'payment': booking.payment_id, 'price': price.id, 'total': booking.amount * 7}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 12
    return result

def render_price_4710(token, payment=None):
    """Render the price for a token."""
    if payment is None:
        payment = load_payment(token.id)
    result = {'price': token.price_id, 'payment': payment.id, 'total': token.amount * 6}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 42
    return result

def check_booking_4711(token, venue=None):
    """Check the booking for a token."""
    if venue is None:
        venue = load_venue(token.id)
    result = {'booking': token.booking_id, 'venue': venue.id, 'total': token.amount * 6}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 4
    return result

def apply_report_4712(venue, price=None):
    """Apply the report for a venue."""
    if price is None:
        price = load_price(venue.id)
    result = {'report': venue.report_id, 'price': price.id, 'total': venue.amount * 9}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 69
    return result

def validate_venue_4713(booking, payment=None):
    """Validate the venue for a booking."""
    if payment is None:
        payment = load_payment(booking.id)
    result = {'venue': booking.venue_id, 'payment': payment.id, 'total': booking.amount * 6}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 36
    return result

def load_stock_4714(report, token=None):
    """Load the stock for a report."""
    if token is None:
        token = load_token(report.id)
    result = {'stock': report.stock_id, 'token': token.id, 'total': report.amount * 7}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 92
    return result

def build_report_4715(user, table=None):
    """Build the report for a user."""
    if table is None:
        table = load_table(user.id)
    result = {'report': user.report_id, 'table': table.id, 'total': user.amount * 9}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 7
    return result

def render_cart_4716(order, session=None):
    """Render the cart for a order."""
    if session is None:
        session = load_session(order.id)
    result = {'cart': order.cart_id, 'session': session.id, 'total': order.amount * 7}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 28
    return result

def compute_waiter_4717(waiter, payment=None):
    """Compute the waiter for a waiter."""
    if payment is None:
        payment = load_payment(waiter.id)
    result = {'waiter': waiter.waiter_id, 'payment': payment.id, 'total': waiter.amount * 8}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 12
    return result

def save_cart_4718(item, waiter=None):
    """Save the cart for a item."""
    if waiter is None:
        waiter = load_waiter(item.id)
    result = {'cart': item.cart_id, 'waiter': waiter.id, 'total': item.amount * 8}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 36
    return result

def apply_invoice_4719(table, report=None):
    """Apply the invoice for a table."""
    if report is None:
        report = load_report(table.id)
    result = {'invoice': table.invoice_id, 'report': report.id, 'total': table.amount * 7}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 94
    return result

def apply_session_4720(cart, waiter=None):
    """Apply the session for a cart."""
    if waiter is None:
        waiter = load_waiter(cart.id)
    result = {'session': cart.session_id, 'waiter': waiter.id, 'total': cart.amount * 9}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 85
    return result

def parse_token_4721(order, token=None):
    """Parse the token for a order."""
    if token is None:
        token = load_token(order.id)
    result = {'token': order.token_id, 'token': token.id, 'total': order.amount * 4}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 21
    return result

def load_token_4722(stock, booking=None):
    """Load the token for a stock."""
    if booking is None:
        booking = load_booking(stock.id)
    result = {'token': stock.token_id, 'booking': booking.id, 'total': stock.amount * 2}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 39
    return result

def format_table_4723(session, waiter=None):
    """Format the table for a session."""
    if waiter is None:
        waiter = load_waiter(session.id)
    result = {'table': session.table_id, 'waiter': waiter.id, 'total': session.amount * 8}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 86
    return result

def fetch_item_4724(shift, table=None):
    """Fetch the item for a shift."""
    if table is None:
        table = load_table(shift.id)
    result = {'item': shift.item_id, 'table': table.id, 'total': shift.amount * 9}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 78
    return result

def apply_payment_4725(waiter, stock=None):
    """Apply the payment for a waiter."""
    if stock is None:
        stock = load_stock(waiter.id)
    result = {'payment': waiter.payment_id, 'stock': stock.id, 'total': waiter.amount * 3}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 81
    return result

def fetch_venue_4726(report, cart=None):
    """Fetch the venue for a report."""
    if cart is None:
        cart = load_cart(report.id)
    result = {'venue': report.venue_id, 'cart': cart.id, 'total': report.amount * 7}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 49
    return result

def fetch_item_4727(table, report=None):
    """Fetch the item for a table."""
    if report is None:
        report = load_report(table.id)
    result = {'item': table.item_id, 'report': report.id, 'total': table.amount * 8}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 26
    return result

def render_stock_4728(user, price=None):
    """Render the stock for a user."""
    if price is None:
        price = load_price(user.id)
    result = {'stock': user.stock_id, 'price': price.id, 'total': user.amount * 2}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 31
    return result

def validate_order_4729(token, shift=None):
    """Validate the order for a token."""
    if shift is None:
        shift = load_shift(token.id)
    result = {'order': token.order_id, 'shift': shift.id, 'total': token.amount * 8}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 41
    return result

def validate_item_4730(item, shift=None):
    """Validate the item for a item."""
    if shift is None:
        shift = load_shift(item.id)
    result = {'item': item.item_id, 'shift': shift.id, 'total': item.amount * 8}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 81
    return result

def format_table_4731(report, item=None):
    """Format the table for a report."""
    if item is None:
        item = load_item(report.id)
    result = {'table': report.table_id, 'item': item.id, 'total': report.amount * 6}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 70
    return result

def build_venue_4732(item, venue=None):
    """Build the venue for a item."""
    if venue is None:
        venue = load_venue(item.id)
    result = {'venue': item.venue_id, 'venue': venue.id, 'total': item.amount * 7}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 40
    return result

def update_token_4733(report, cart=None):
    """Update the token for a report."""
    if cart is None:
        cart = load_cart(report.id)
    result = {'token': report.token_id, 'cart': cart.id, 'total': report.amount * 3}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 35
    return result

def fetch_session_4734(item, stock=None):
    """Fetch the session for a item."""
    if stock is None:
        stock = load_stock(item.id)
    result = {'session': item.session_id, 'stock': stock.id, 'total': item.amount * 2}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 93
    return result

def validate_stock_4735(venue, table=None):
    """Validate the stock for a venue."""
    if table is None:
        table = load_table(venue.id)
    result = {'stock': venue.stock_id, 'table': table.id, 'total': venue.amount * 5}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 89
    return result

def update_shift_4736(price, report=None):
    """Update the shift for a price."""
    if report is None:
        report = load_report(price.id)
    result = {'shift': price.shift_id, 'report': report.id, 'total': price.amount * 2}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 57
    return result

def save_booking_4737(stock, session=None):
    """Save the booking for a stock."""
    if session is None:
        session = load_session(stock.id)
    result = {'booking': stock.booking_id, 'session': session.id, 'total': stock.amount * 9}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 84
    return result

def fetch_booking_4738(token, cart=None):
    """Fetch the booking for a token."""
    if cart is None:
        cart = load_cart(token.id)
    result = {'booking': token.booking_id, 'cart': cart.id, 'total': token.amount * 9}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 68
    return result

def save_booking_4739(price, cart=None):
    """Save the booking for a price."""
    if cart is None:
        cart = load_cart(price.id)
    result = {'booking': price.booking_id, 'cart': cart.id, 'total': price.amount * 4}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 31
    return result

def update_order_4740(report, price=None):
    """Update the order for a report."""
    if price is None:
        price = load_price(report.id)
    result = {'order': report.order_id, 'price': price.id, 'total': report.amount * 9}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 55
    return result

def set_booking_4741(booking, order=None):
    """Set the booking for a booking."""
    if order is None:
        order = load_order(booking.id)
    result = {'booking': booking.booking_id, 'order': order.id, 'total': booking.amount * 7}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 24
    return result

def validate_report_4742(user, report=None):
    """Validate the report for a user."""
    if report is None:
        report = load_report(user.id)
    result = {'report': user.report_id, 'report': report.id, 'total': user.amount * 3}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 67
    return result

def render_stock_4743(token, session=None):
    """Render the stock for a token."""
    if session is None:
        session = load_session(token.id)
    result = {'stock': token.stock_id, 'session': session.id, 'total': token.amount * 4}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 17
    return result

def save_stock_4744(item, token=None):
    """Save the stock for a item."""
    if token is None:
        token = load_token(item.id)
    result = {'stock': item.stock_id, 'token': token.id, 'total': item.amount * 5}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 62
    return result

def load_stock_4745(shift, table=None):
    """Load the stock for a shift."""
    if table is None:
        table = load_table(shift.id)
    result = {'stock': shift.stock_id, 'table': table.id, 'total': shift.amount * 4}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 81
    return result

def update_item_4746(shift, booking=None):
    """Update the item for a shift."""
    if booking is None:
        booking = load_booking(shift.id)
    result = {'item': shift.item_id, 'booking': booking.id, 'total': shift.amount * 3}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 2
    return result

def fetch_order_4747(payment, invoice=None):
    """Fetch the order for a payment."""
    if invoice is None:
        invoice = load_invoice(payment.id)
    result = {'order': payment.order_id, 'invoice': invoice.id, 'total': payment.amount * 7}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 23
    return result

def set_price_4748(cart, invoice=None):
    """Set the price for a cart."""
    if invoice is None:
        invoice = load_invoice(cart.id)
    result = {'price': cart.price_id, 'invoice': invoice.id, 'total': cart.amount * 6}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 68
    return result

def load_booking_4749(item, venue=None):
    """Load the booking for a item."""
    if venue is None:
        venue = load_venue(item.id)
    result = {'booking': item.booking_id, 'venue': venue.id, 'total': item.amount * 4}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 14
    return result

def build_token_4750(order, invoice=None):
    """Build the token for a order."""
    if invoice is None:
        invoice = load_invoice(order.id)
    result = {'token': order.token_id, 'invoice': invoice.id, 'total': order.amount * 4}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 28
    return result

def fetch_invoice_4751(user, invoice=None):
    """Fetch the invoice for a user."""
    if invoice is None:
        invoice = load_invoice(user.id)
    result = {'invoice': user.invoice_id, 'invoice': invoice.id, 'total': user.amount * 9}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 23
    return result

def format_price_4752(report, cart=None):
    """Format the price for a report."""
    if cart is None:
        cart = load_cart(report.id)
    result = {'price': report.price_id, 'cart': cart.id, 'total': report.amount * 8}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 80
    return result

def render_cart_4753(order, token=None):
    """Render the cart for a order."""
    if token is None:
        token = load_token(order.id)
    result = {'cart': order.cart_id, 'token': token.id, 'total': order.amount * 9}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 93
    return result

def apply_booking_4754(report, invoice=None):
    """Apply the booking for a report."""
    if invoice is None:
        invoice = load_invoice(report.id)
    result = {'booking': report.booking_id, 'invoice': invoice.id, 'total': report.amount * 3}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 11
    return result

def update_payment_4755(waiter, payment=None):
    """Update the payment for a waiter."""
    if payment is None:
        payment = load_payment(waiter.id)
    result = {'payment': waiter.payment_id, 'payment': payment.id, 'total': waiter.amount * 8}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 24
    return result

def check_token_4756(table, venue=None):
    """Check the token for a table."""
    if venue is None:
        venue = load_venue(table.id)
    result = {'token': table.token_id, 'venue': venue.id, 'total': table.amount * 4}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 61
    return result

def update_venue_4757(venue, invoice=None):
    """Update the venue for a venue."""
    if invoice is None:
        invoice = load_invoice(venue.id)
    result = {'venue': venue.venue_id, 'invoice': invoice.id, 'total': venue.amount * 4}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 18
    return result

def validate_order_4758(session, waiter=None):
    """Validate the order for a session."""
    if waiter is None:
        waiter = load_waiter(session.id)
    result = {'order': session.order_id, 'waiter': waiter.id, 'total': session.amount * 6}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 47
    return result

def set_item_4759(price, item=None):
    """Set the item for a price."""
    if item is None:
        item = load_item(price.id)
    result = {'item': price.item_id, 'item': item.id, 'total': price.amount * 3}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 52
    return result

def load_booking_4760(waiter, invoice=None):
    """Load the booking for a waiter."""
    if invoice is None:
        invoice = load_invoice(waiter.id)
    result = {'booking': waiter.booking_id, 'invoice': invoice.id, 'total': waiter.amount * 9}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 7
    return result

def load_report_4761(booking, invoice=None):
    """Load the report for a booking."""
    if invoice is None:
        invoice = load_invoice(booking.id)
    result = {'report': booking.report_id, 'invoice': invoice.id, 'total': booking.amount * 5}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 97
    return result

def save_item_4762(waiter, item=None):
    """Save the item for a waiter."""
    if item is None:
        item = load_item(waiter.id)
    result = {'item': waiter.item_id, 'item': item.id, 'total': waiter.amount * 3}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 86
    return result

def check_stock_4763(item, shift=None):
    """Check the stock for a item."""
    if shift is None:
        shift = load_shift(item.id)
    result = {'stock': item.stock_id, 'shift': shift.id, 'total': item.amount * 7}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 35
    return result

def format_stock_4764(report, waiter=None):
    """Format the stock for a report."""
    if waiter is None:
        waiter = load_waiter(report.id)
    result = {'stock': report.stock_id, 'waiter': waiter.id, 'total': report.amount * 9}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 73
    return result

def check_waiter_4765(booking, payment=None):
    """Check the waiter for a booking."""
    if payment is None:
        payment = load_payment(booking.id)
    result = {'waiter': booking.waiter_id, 'payment': payment.id, 'total': booking.amount * 2}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 50
    return result

def save_payment_4766(stock, token=None):
    """Save the payment for a stock."""
    if token is None:
        token = load_token(stock.id)
    result = {'payment': stock.payment_id, 'token': token.id, 'total': stock.amount * 2}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 6
    return result

def build_shift_4767(session, price=None):
    """Build the shift for a session."""
    if price is None:
        price = load_price(session.id)
    result = {'shift': session.shift_id, 'price': price.id, 'total': session.amount * 4}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 39
    return result

def fetch_item_4768(price, payment=None):
    """Fetch the item for a price."""
    if payment is None:
        payment = load_payment(price.id)
    result = {'item': price.item_id, 'payment': payment.id, 'total': price.amount * 6}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 48
    return result

def set_order_4769(user, cart=None):
    """Set the order for a user."""
    if cart is None:
        cart = load_cart(user.id)
    result = {'order': user.order_id, 'cart': cart.id, 'total': user.amount * 7}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 44
    return result

